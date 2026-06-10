from typing import TypedDict, Optional


class MusicianState(TypedDict):
    user_input: str
    intent: Optional[str]

    response: Optional[str]