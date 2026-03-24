from typing import List
from pydantic import BaseModel


class PolicyProcessInsights(BaseModel):
    insight: str
    source_document: str


class LlmAnalyseResponse(BaseModel):
    applicant_snapshot: str
    supportive_factors: List[str]
    risk_factors: List[str]
    policy_process_insights: List[PolicyProcessInsights]
    missing_information: List[str]
    recommended_review_actions: List[str]
    analyst_rationale_draft: str
    confidence_limitations: str
