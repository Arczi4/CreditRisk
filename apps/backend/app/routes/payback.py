from typing import List

from fastapi import APIRouter

from app.core.logging_config import get_logger
from app.models.payback_models import PaybackRequest, PaybackEndpointResponse
from app.services.payback_service import payback_service
from app.services.analysis_service import analysis_service

logger = get_logger(__name__)

router = APIRouter(prefix="/payback", tags=["payback"])


@router.post("/single", response_model=PaybackEndpointResponse)
async def payback(
    request: PaybackRequest,
):
    logger.info(f"Got payback request {request.request_id}")
    try:
        # TODO: create dataclass
        loan_decision, predict_proba, model_signals = payback_service.payback(request)
    except Exception as e:
        raise Exception(
            f"Errod during predicting payback probability for request: {request.request_id}. ERROR: {e}"
        )
    logger.info(
        f"Sucessfully processed payback probability for request: {request.request_id}"
    )

    try:
        parsed_analysis_response = analysis_service.analyse(request, model_signals)
    except:
        raise Exception

    return PaybackEndpointResponse(
        loan_decision=loan_decision,
        payback_proba=predict_proba,
        insights=parsed_analysis_response,  # TODO: add additional insights
    )
