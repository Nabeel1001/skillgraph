from fastapi import APIRouter
from app.services.graph_service import GraphService

router = APIRouter(
    prefix="/graph",
    tags=["Graph"]
)

@router.get("/person/{person_id}")
def person_graph(person_id: int):
    return GraphService.get_person_graph(person_id)