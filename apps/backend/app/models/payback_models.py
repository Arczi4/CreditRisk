from typing import List
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_serializer, ConfigDict


class PaybackRequest(BaseModel):
    """Payback payload request model"""

    request_id: UUID = Field(default_factory=uuid4, description="Unique request ID")

    gender: str = Field(..., min_length=1, description="Borrower gender")
    marital_status: str = Field(
        ..., min_length=1, description="Borrower marital status"
    )
    education_level: str = Field(
        ..., min_length=1, description="Borrower education level"
    )
    employment_status: str = Field(
        ..., min_length=1, description="Borrower employment status"
    )
    loan_purpose: str = Field(..., min_length=1, description="Borrower loan purpose")
    grade_subgrade: str = Field(
        ..., min_length=1, description="Borrower grade subgrade"
    )

    annual_income: float = Field(..., ge=0.0, description="Borrower annual income")
    debt_to_income_ratio: float = Field(
        ..., ge=0.0, description="Borrower debt to income ratio"
    )
    credit_score: float = Field(..., ge=0.0, description="Borrower credit score")
    loan_amount: float = Field(..., ge=0.0, description="Borrower loan amount")
    interest_rate: float = Field(..., ge=0.0, description="Borrower interest rate")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "gender": "Female",
                "marital_status": "Single",
                "education_level": "High School",
                "employment_status": "Self-employed",
                "loan_purpose": "Other",
                "grade_subgrade": "C3",
                "annual_income": 29367.99,
                "debt_to_income_ratio": 0.084,
                "credit_score": 736,
                "loan_amount": 2528.42,
                "interest_rate": 13.67,
            }
        }
    )


class PaybackResponse(BaseModel):
    """Credit score response with payback proba and additional analysis"""

    loan_paid_back: bool = Field(
        default=False,
        description="True/False of prediction if loan will be paid back. True when predict proba thershold is met",
    )
    payback_proba: float = Field(..., ge=0.0, le=1.0, description="Payback probability")
    insights: List[str] = Field(..., description="Additional insights provided by AI")

    @field_serializer("payback_proba", when_used="always")
    def serialize_payback_proba(self, value: float) -> float:
        return round(value, 4)

    class Config:
        json_schema_extra = {
            "example": {
                "loan_paid_back": False,
                "payback_proba": 0.8,
                "insights": ["some insight1", "some insight2"],
            }
        }
