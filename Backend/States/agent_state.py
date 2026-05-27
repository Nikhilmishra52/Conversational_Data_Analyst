from typing import Optional,List,TypedDict
from langchain_core.messages import BaseMessage

class AnalyticsGraphState(TypedDict):
    # Shared across all nodes
    thread_id: str
    conversation_id:      str
    user_message:         str
    conversation_history: List[BaseMessage]   # full chat history
    final_response:       Optional[dict]
    orchestrator_ctx: Optional[dict]
    data_engineer_ctx: Optional[dict]
    data_scientist_ctx: Optional[dict]
    synthesizer_ctx: Optional[dict]