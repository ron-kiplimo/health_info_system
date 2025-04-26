from fastapi import FastAPI
from . import models
from .database import engine
from .api import endpoints

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include our API router
app.include_router(endpoints.router)

@app.get("/")
def read_root():
    return {"message": "Health Information System is running"}
