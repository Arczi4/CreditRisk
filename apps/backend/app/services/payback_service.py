from typing import Tuple

import pandas as pd
from app.models.payback_models import LoanDecisionEnum, PaybackRequest
from app.ml.ml_processor import ml_processor
from app.ml.model_config import model_config

from app.core.logging_config import get_logger

logger = get_logger(__name__)


COLUMN_ORDER = [
    "gender",
    "marital_status",
    "education_level",
    "employment_status",
    "loan_purpose",
    "grade_subgrade",
    "annual_income",
    "debt_to_income_ratio",
    "credit_score",
    "loan_amount",
    "interest_rate",
]


class PaybackService:
    """
    Uses trained model to predict credit risk scoring based on provided data
    """

    def payback(self, request: PaybackRequest) -> Tuple[LoanDecisionEnum, float]:
        features = self.__parse_payback_to_dataframe(request)

        logger.info(
            f"Predicting payback probability for request ID: {request.request_id}..."
        )
        try:
            payback_proba = ml_processor.score_single(features)
            loan_decision = self.get_loan_decision(payback_proba)

        # TODO: improve error handling.
        except Exception as e:
            logger.error(
                f"Error during predicting payback probability for request ID: {request.request_id}. ERROR: {e}"
            )
            return LoanDecisionEnum.REJECT, 0.0

        logger.info(
            f"Predicting payback probability for request ID: {request.request_id} done."
        )

        return loan_decision, payback_proba

    def batch_payback():
        raise NotImplementedError("This feature is not implemented yet.")

    @staticmethod
    def get_loan_decision(payback_proba: float) -> LoanDecisionEnum:
        if payback_proba >= model_config.APPROVE_THRESHOLD:
            return LoanDecisionEnum.APPROVE
        if payback_proba >= model_config.REVIEW_THRESHOLD:
            return LoanDecisionEnum.REVIEW

        return LoanDecisionEnum.REJECT

    @staticmethod
    def __parse_payback_to_dataframe(request: PaybackRequest) -> pd.DataFrame:
        row = {
            col: [getattr(request, col)] for col in COLUMN_ORDER if col != "request_id"
        }
        return pd.DataFrame(row)


payback_service = PaybackService()
