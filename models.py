from pydantic import BaseModel

class Term(BaseModel):
    keyword: str
    description: str