from fastapi import APIRouter

from backend.schemas.health import (
    HealthRequest,
    HealthResponse,
)

from backend.services.health_service import calculate_health

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.post("/", response_model=HealthResponse)
def get_health(data: HealthRequest):
    return calculate_health(data)