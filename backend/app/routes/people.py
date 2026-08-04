from fastapi import APIRouter
from app.services.graph_service import GraphService

router = APIRouter(prefix="/people", tags=["People"])


@router.get("")
def get_people():
    return GraphService.get_all_people()

@router.get("/{person_id}")
def get_person(person_id: int):
    return GraphService.get_person_profile(person_id)