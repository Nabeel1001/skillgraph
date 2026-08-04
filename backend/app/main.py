from fastapi import FastAPI
from app.db.connection import verify_connection
from app.routes.people import router as people_router
from app.routes.dashboard import router as dashboard_router
from app.routes.companies import router as company_router
from app.routes.graph import router as graph_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SkillGraph API")

app.include_router(people_router)
app.include_router(dashboard_router)
app.include_router(company_router)
app.include_router(graph_router)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "SkillGraph API is running"}


@app.get("/health")
def health():
    return {
        "database": verify_connection()
    }