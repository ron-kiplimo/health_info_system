from fastapi import FastAPI
from . import models
from .database import engine
from .api import endpoints

models.Base.metadata.create_all(bind=engine)

# Customized FastAPI app
app = FastAPI(
    title="Health Information System",
    description="An API for managing clients and health programs.",
    version="1.0.0",
    contact={
        "name": "Ronald Kibet Kiplimo",
        "email": "rkkiplimo@gmail.com",
        "url": "https://your-portfolio-or-github-link.com",  # optional
    },
)

# Include API routes
app.include_router(endpoints.router)

@app.get("/")
def read_root():
    return {"message": "Health Information System is running"}
