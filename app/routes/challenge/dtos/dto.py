from typing import List, Optional, Any, Literal
from pydantic import BaseModel, Field, field_validator

from app.schemas.schema import Number


class ChallengeRequestDTO(BaseModel):
    operation: Literal["sum", "subtract", "multiply", "divide"] = Field(
        ..., description="Operation to perform: sum, subtract, multiply, divide."
    )
    operands: List[Number] = Field(
        ..., min_items=2, description="Operands for the operation."
    )

    @field_validator("operands")
    @classmethod
    def validate_operands(cls, v: List[Number]):
        if len(v) < 2:
            raise ValueError("At least two operands are required.")
        if not all(isinstance(n, (int, float)) for n in v):
            raise ValueError("All operands must be numbers.")
        return v


class ChallengeResponseDTO(BaseModel):
    success: bool = Field(..., description="Indicates if the operation was successful.")
    message: Optional[str] = Field(
        None, description="Contextual message for the operation."
    )
    data: Optional[Any] = Field(
        None, description="Resulting user object or related data."
    )
