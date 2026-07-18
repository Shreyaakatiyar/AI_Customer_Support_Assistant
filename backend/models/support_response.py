from pydantic import BaseModel

class SupportResponse(BaseModel):
    category: str
    confidence: int
    needs_human: bool
    answer: str