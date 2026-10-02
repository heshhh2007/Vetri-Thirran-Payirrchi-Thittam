from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import Base, engine
from app.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FitBuddy AI Plan Generator")

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)