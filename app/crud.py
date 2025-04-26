from sqlalchemy.orm import Session
from . import models, schemas

# ====== Program CRUD ======

def create_program(db: Session, program: schemas.ProgramCreate):
    db_program = models.Program(name=program.name)
    db.add(db_program)
    db.commit()
    db.refresh(db_program)
    return db_program

def get_program_by_name(db: Session, name: str):
    return db.query(models.Program).filter(models.Program.name == name).first()

def get_programs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Program).offset(skip).limit(limit).all()

# ====== Client CRUD ======

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(
        name=client.name,
        email=client.email,
        phone=client.phone
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()

def get_client_by_email(db: Session, email: str):
    return db.query(models.Client).filter(models.Client.email == email).first()

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()

def enroll_client_in_program(db: Session, client_id: int, program_id: int):
    client = get_client(db, client_id)
    program = db.query(models.Program).filter(models.Program.id == program_id).first()
    if client and program:
        client.programs.append(program)
        db.commit()
        db.refresh(client)
        return client
    return None
