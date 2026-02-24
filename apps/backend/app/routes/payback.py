from fastapi import APIRouter

from app.core.logging_config import get_logger
from app.models.payback_models import PaybackRequest, PaybackResponse

logger = get_logger(__name__)

router = APIRouter(prefix="/payback", tags=["payback"])


@router.post("/", response_model=PaybackResponse)
async def payback(
    request: PaybackRequest,
):
    logger.info(f"Got payback request {request}")
    return PaybackResponse(loan_paid_back=False, payback_proba=0.0, insights=["none"])
