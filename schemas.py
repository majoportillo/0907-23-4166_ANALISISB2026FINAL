from pydantic import BaseModel
from typing import Optional

class IncidenteCreate(BaseModel):
    descripcion: str
    severidad: str
    tecnico_id: Optional[int] = None

class IncidenteResponse(BaseModel):  # Asegúrate que el nombre sea este
    id: int
    descripcion: str
    severidad: str
    estado: str
    tecnico_id: Optional[int] = None
    
    class Config:
        from_attributes = True