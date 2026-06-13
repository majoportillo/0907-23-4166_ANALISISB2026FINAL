from sqlalchemy import Column, Integer, String, Enum
from database import Base
import enum

class EstadoEnum(str, enum.Enum):
    registrado = "Registrado"
    asignado = "Asignado"
    en_progreso = "En progreso"
    resuelto = "Resuelto"
    cerrado = "Cerrado"
    escalado = "Escalado"

class Incidente(Base):
    __tablename__ = "incidentes"
    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)
    severidad = Column(String)
    estado = Column(Enum(EstadoEnum), default=EstadoEnum.registrado)
    tecnico_id = Column(Integer, nullable=True)