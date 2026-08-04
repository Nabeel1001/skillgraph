from fastapi import APIRouter
from app.services.person_service import PersonService

router = APIRouter(prefix="/people", tags=["People"])


@router.get("")
def get_people():
    return PersonService.get_all()


@router.get("/{person_id}")
def get_person(person_id: int):
    return PersonService.get_profile(person_id)