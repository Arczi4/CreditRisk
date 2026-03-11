from typing import List

from fastapi import APIRouter

from app.core.logging_config import get_logger
from app.models.payback_models import PaybackRequest, PaybackResponse
from app.services.payback_service import payback_service
from app.ml.model_config import model_config

logger = get_logger(__name__)

router = APIRouter(prefix="/payback", tags=["payback"])


@router.post("/single", response_model=PaybackResponse)
async def payback(
    request: PaybackRequest,
):
    logger.info(f"Got payback request {request.request_id}")
    try:
        predict_proba = payback_service.payback(request)
    except Exception as e:
        raise Exception(
            f"Errod during predicting payback probability for request: {request.request_id}. ERROR: {e}"
        )
    logger.info(
        f"Sucessfully processed payback probability for request: {request.request_id}"
    )

    return PaybackResponse(
        loan_paid_back=(
            True if predict_proba >= model_config.MODEL_SCORE_THRESHOLD else False
        ),
        payback_proba=predict_proba,
        insights=["none"],  # TODO: add additional insights
    )
