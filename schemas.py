from pydantic import BaseModel, ConfigDict
from typing import Optional

class IncidenteCreate(BaseModel):
    descripcion: str
    severidad: str
    tecnico_id: Optional[int] = None

class IncidenteResponse(BaseModel):
    id: int
    descripcion: str
    severidad: str
    estado: str
    tecnico_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)