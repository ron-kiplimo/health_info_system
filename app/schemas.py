from pydantic import BaseModel
from typing import List, Optional

# ======== PROGRAM SCHEMAS ========

class ProgramBase(BaseModel):
    name: str

class ProgramCreate(ProgramBase):
    pass

class Program(ProgramBase):
    id: int
    class Config:
        orm_mode = True

# ======== CLIENT SCHEMAS ========

class ClientBase(BaseModel):
    name: str
    email: str
    phone: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int
    programs: List[Program] = []
    class Config:
        orm_mode = True
