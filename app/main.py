from fastapi import FastAPI
from . import models
from .database import engine
from .api import endpoints

models.Base.metadata.create_all(bind=engine)

# Customized FastAPI app
app = FastAPI(
    docs_url="/api-docs",        # Instead of /docs
    redoc_url="/redocs",          # Optional second documentation at /redocs
    openapi_url="/openapi.json",  # OpenAPI schema URL
    title="Health Information System",
    description="An API for managing clients and health programs.",
    version="1.0.0",
    contact={
        "name": "Ronald Kibet Kiplimo",
        "email": "rkkiplimo@gmail.com",
        "url": "https://your-portfolio-or-github-link.com",
    },
)