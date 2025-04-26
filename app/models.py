from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Association table for Many-to-Many (Client <-> Program)
client_program = Table(
    "client_program",
    Base.metadata,
    Column("client_id", Integer, ForeignKey("clients.id")),
    Column("program_id", Integer, ForeignKey("programs.id"))
)

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)

    programs = relationship("Program", secondary=client_program, back_populates="clients")


class Program(Base):
    __tablename__ = "programs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    clients = relationship("Client", secondary=client_program, back_populates="programs")
