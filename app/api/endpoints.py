from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas
from ..database import SessionLocal

router = APIRouter()

# Dependency: get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a program
@router.post("/programs/", response_model=schemas.Program)
def create_program(program: schemas.ProgramCreate, db: Session = Depends(get_db)):
    db_program = crud.get_program_by_name(db, name=program.name)
    if db_program:
        raise HTTPException(status_code=400, detail="Program already exists")
    return crud.create_program(db=db, program=program)

# Create a client
@router.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    db_client = crud.get_client_by_email(db, email=client.email)
    if db_client:
        raise HTTPException(status_code=400, detail="Client already exists")
    return crud.create_client(db=db, client=client)

# Enroll client in a program
@router.post("/clients/{client_id}/enroll/{program_id}", response_model=schemas.Client)
def enroll_client_in_program(client_id: int, program_id: int, db: Session = Depends(get_db)):
    client = crud.enroll_client_in_program(db, client_id, program_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client or Program not found")
    return client

# Get list of clients
@router.get("/clients/", response_model=List[schemas.Client])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = crud.get_clients(db, skip=skip, limit=limit)
    return clients

# Get single client by ID
@router.get("/clients/{client_id}", response_model=schemas.Client)
def read_client(client_id: int, db: Session = Depends(get_db)):
    client = crud.get_client(db, client_id=client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client
