import streamlit as st
import pandas as pd

from database.db import init_db
from graph.workflow import run_workflow

from tools.payment_tools import (
    get_pending_payments,
    get_all_gigs,
    get_total_gigs
)

from tools.memory_tools import get_all_memories

# ---------------------------------
# INIT
# ---------------------------------

init_db()

st.set_page_config(
    page_title="Moksha Operations Copilot",
    page_icon="🎸",
    layout="wide"
)

# ---------------------------------
# DATA
# ---------------------------------

memories = dict(get_all_memories())

pending = get_pending_payments()

all_gigs = get_all_gigs()

total_gigs = get_total_gigs()

total_pending = sum(
    row[1] for row in pending
) if pending else 0

band_members = [
    "vocalist",
    "guitarist",
    "bassist",
    "drummer",
    "keyboardist",
    "flutist"
]

member_count = sum(
    1 for member in band_members
    if memories.get(member)
)

venue_count = len(
    set(row[0] for row in all_gigs)
) if all_gigs else 0

# ---------------------------------
# SIDEBAR
# ---------------------------------

st.sidebar.image(
    "assets/moksha_logo.png",
    use_container_width=True
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "AI Copilot",
        "Payments",
        "Gigs",
        "Band Profile"
    ]
)

# =================================
# AI COPILOT
# =================================

if page == "AI Copilot":

    st.title("Operations Copilot")

    st.caption(
        "Manage gigs, payments, payouts and performance operations using AI."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Pending Amount",
            f"₹{total_pending:,.0f}"
        )

    with col2:
        st.metric(
            "Venues",
            venue_count
        )

    with col3:
        st.metric(
            "Band Members",
            member_count
        )

    with col4:
        st.metric(
            "Total Gigs",
            total_gigs
        )

    st.divider()

    st.subheader("Quick Actions")

    q1, q2, q3, q4 = st.columns(4)

    if q1.button("💰 Show Payments"):
        st.session_state["prompt"] = "Show me pending payments"

    if q2.button("📩 Follow-Up"):
        st.session_state["prompt"] = "Generate payment follow-up for XYZ"

    if q3.button("🧾 Calculate Payout"):
        st.session_state["prompt"] = "Calculate payout for Hard Rock Cafe"

    if q4.button("🎤 Create Setlist"):
        st.session_state["prompt"] = "Create a setlist for a college fest"

    st.divider()

    default_prompt = st.session_state.get(
        "prompt",
        ""
    )

    user_input = st.text_area(
        "Ask Your Copilot",
        value=default_prompt,
        height=120,
        placeholder="Add gig at XYZ on June 20 for 50000"
    )

    if st.button(
        "Run Copilot",
        use_container_width=True
    ):

        if user_input.strip():

            with st.spinner("Processing..."):

                result = run_workflow(
                    user_input
                )

            st.success("Response")

            st.markdown(
                result["response"]
            )

# =================================
# PAYMENTS
# =================================

elif page == "Payments":

    st.title("💰 Pending Payments")

    if not pending:

        st.success(
            "No pending payments."
        )

    else:

        st.metric(
            "Total Outstanding",
            f"₹{total_pending:,.0f}"
        )

        st.divider()

        for venue, amount, status in pending:

            col1, col2 = st.columns(
                [4, 1]
            )

            with col1:
                st.markdown(
                    f"### {venue}"
                )

            with col2:
                st.markdown(
                    f"### ₹{amount:,.0f}"
                )

# =================================
# GIGS
# =================================

elif page == "Gigs":

    st.title("🎤 Gig Tracker")

    if not all_gigs:

        st.info(
            "No gigs found."
        )

    else:

        gigs_df = pd.DataFrame(
            all_gigs,
            columns=[
                "Venue",
                "Date",
                "Fee",
                "Status"
            ]
        )

        gigs_df["Fee"] = gigs_df[
            "Fee"
        ].apply(
            lambda x: f"₹{x:,.0f}"
        )

        st.dataframe(
            gigs_df,
            use_container_width=True,
            hide_index=True
        )

# =================================
# BAND PROFILE
# =================================

elif page == "Band Profile":

    st.title("👥 Band Profile")

    for key, value in memories.items():

        st.markdown(
            f"**{key.replace('_', ' ').title()}**"
        )

        st.write(value)

        st.divider()