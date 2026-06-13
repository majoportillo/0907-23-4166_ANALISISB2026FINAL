from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database, schemas

# Crear tablas
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependencia para obtener la sesión de BD
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint POST: Crear incidente
@app.post("/incidentes/", response_model=schemas.IncidenteResponse)
def crear_incidente(incidente: schemas.IncidenteCreate, db: Session = Depends(get_db)):
    db_incidente = models.Incidente(**incidente.model_dump())
    db.add(db_incidente)
    db.commit()
    db.refresh(db_incidente)
    return db_incidente

# Endpoint GET: Ver todos los incidentes
@app.get("/incidentes/")
def listar_incidentes(db: Session = Depends(get_db)):
    return db.query(models.Incidente).all()

# Endpoint PUT: Actualizar estado del incidente
@app.put("/incidentes/{id}/estado/{nuevo_estado}")
def actualizar_estado(id: int, nuevo_estado: str, db: Session = Depends(get_db)):
    incidente = db.query(models.Incidente).filter(models.Incidente.id == id).first()
    if not incidente:
        raise HTTPException(status_code=404, detail="Incidente no encontrado")
    incidente.estado = nuevo_estado
    db.commit()
    return {"mensaje": "Estado actualizado exitosamente"}