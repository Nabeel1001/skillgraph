from fastapi import FastAPI
from app.db.connection import verify_connection
from app.routes.people import router as people_router

app = FastAPI(title="SkillGraph API")
app.include_router(people_router)


@app.get("/")
def root():
    return {"message": "SkillGraph API is running"}


@app.get("/health")
def health():
    return {
        "database": verify_connection()
    }