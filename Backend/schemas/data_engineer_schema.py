from pydantic import BaseModel
from typing import Optional

class DataEngineerContext(BaseModel):
    discovered_schema: dict
    generated_sql: str
    query_results: list
    provenance: dict
    error: Optional[str]