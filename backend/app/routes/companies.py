from fastapi import APIRouter
from app.services.company_service import CompanyService

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.get("")
def get_companies():
    return CompanyService.get_all()