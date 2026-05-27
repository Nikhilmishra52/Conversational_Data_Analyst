from pydantic import BaseModel
class OrchestratorContext(BaseModel):
    intent: str
    extracted_entities: dict
    routing_decision: str