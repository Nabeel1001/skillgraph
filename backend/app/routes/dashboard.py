from fastapi import APIRouter
from app.services.dashboard_service import DashboardService

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/stats")
def stats():
    return DashboardService.get_stats()