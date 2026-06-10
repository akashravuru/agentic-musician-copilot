# 🎸 Agentic Musician Copilot

An AI-powered operations assistant built for live bands and performing artists.

Agentic Musician Copilot helps manage gigs, track payments, calculate payouts, generate follow-up messages, and maintain band information using natural language commands.

Built for my band **Moksha**, this project demonstrates how LLM-powered agents can automate real-world operational workflows.

---

## Features

### 🎤 Gig Management

Add gigs using natural language.

Example:

```text
Add gig at Hard Rock Cafe on June 30 for 75000
```

The system extracts:

* Venue
* Date
* Fee

and stores them in a SQLite database.

---

### 💰 Payment Tracking

Track outstanding payments across venues.

Example:

```text
Show me pending payments
```

Returns:

* Venue
* Pending Amount
* Payment Status

---

### 📩 AI Payment Follow-Ups

Generate professional payment reminders.

Example:

```text
Generate payment follow-up for XYZ
```

Output:

A WhatsApp-ready payment follow-up message generated using Gemini.

---

### 🧾 Payout Calculator

Automatically calculate band payouts.

Example:

```text
Calculate payout for Hard Rock Cafe
```

Calculates:

* Venue Fee
* Sound Engineer Share
* Band Pool
* Per Performer Amount

---

### ✅ Payment Reconciliation

Update payment status using natural language.

Examples:

```text
Prism has paid

Received payment from XYZ

Hard Rock Cafe settled payment
```

The system automatically updates the database and removes paid gigs from the pending payments list.

---

### 🎵 Setlist Generation

Generate performance setlists using AI.

Example:

```text
Create a setlist for a college fest
```

---

### 👥 Band Knowledge Base

Store and retrieve information about:

* Band Members
* Roles
* Managers
* Operational Notes

---

### 📊 Streamlit Dashboard

Includes:

* Pending Amount KPI
* Venue Count
* Band Member Count
* Total Gigs KPI
* Gig Tracker
* Payment Dashboard
* AI Copilot Interface

---

## Architecture

```text
User
  ↓
Streamlit UI
  ↓
Router Agent
  ↓
Intent Detection
  ↓
Specialized Agents
     ├── Gig Creator Agent
     ├── Payment Agent
     ├── Payment Follow-Up Agent
     ├── Payment Reconciliation Agent
     ├── Payout Agent
     └── Setlist Agent
  ↓
SQLite Database
```

---

## Tech Stack

* Python
* Streamlit
* Google Gemini
* SQLite
* Agent-Based Workflow Architecture

---

## Example Prompts

```text
Add gig at XYZ on June 20 for 50000

Show me pending payments

Generate payment follow-up for XYZ

Calculate payout for Hard Rock Cafe

Prism has paid

Create a setlist for a college fest
```

---

## Future Improvements

* Calendar Integration
* WhatsApp Integration
* Venue Analytics Dashboard
* Monthly Revenue Reports
* Multi-Band Support
* Cloud Database
* User Authentication

---

## Author

Akash Ravuru

Built as part of an Applied AI Engineering portfolio focused on agentic systems, workflow automation, and real-world AI applications.
