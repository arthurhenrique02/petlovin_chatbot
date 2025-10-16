from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(..., example="Qual a melhor ração para cachorro?")
