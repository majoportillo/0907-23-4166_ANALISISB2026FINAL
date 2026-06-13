# María José del Carmen Portillo López 0907-23-4166 ANALISISB2026FINAL

#Historias de usuario - NetGuard GT

### 1. Historia de usuario: Gestión de Registro de Incidentes

**Requerimiento funcional y no funcional**
Como técnico de soporte, quiero registrar nuevos incidentes de red con su respectiva severidad, para que puedan ser gestionados por el equipo.

**Criterios de Aceptación Funcionales**
· El sistema permite crear un incidente con campos: ID, descripción, severidad (Baja, Media, Alta, Crítica, Urgente), técnico asignado (opcional) y estado inicial 'Registrado'.
· El sistema valida que la severidad sea obligatoria.

**No Funcionales**
· La API debe responder en menos de 200ms.
· Validación de campos obligatorios en el lado del servidor.

**Priorización:** Alta

---
### 2. Historia de usuario: Asignación de Incidentes a Técnicos

**Requerimiento funcional y no funcional**
Como coordinador, quiero asignar un incidente a un técnico disponible, para asegurar su pronta resolución.

**Criterios de Aceptación Funcionales**
· El sistema cambia el estado de 'Registrado' a 'Asignado'.
· El sistema valida que el técnico tenga la especialidad necesaria para el tipo de incidente.
· No se puede asignar si el técnico ya tiene 3 incidentes activos.

**No Funcionales**
· Verificación de reglas de negocio antes de persistir el cambio de estado.

**Priorización:** Alta

---
### 3. Historia de usuario: Control de Carga de Trabajo del Técnico

**Requerimiento funcional y no funcional**
Como sistema, quiero verificar que un técnico no supere los 3 incidentes activos simultáneos, para garantizar la calidad del servicio.

**Criterios de Aceptación Funcionales**
· El sistema bloquea la asignación si el conteo de incidentes con estado 'Registrado', 'Asignado' o 'En progreso' es igual a 3 para ese técnico.

**No Funcionales**
· La consulta de carga de trabajo debe ser eficiente.

**Priorización:** Alta

---
### 4. Historia de usuario: Transición de Estados de Incidentes

**Requerimiento funcional y no funcional**
Como técnico, quiero actualizar el estado de mi incidente, para reflejar el progreso real del trabajo.

**Criterios de Aceptación Funcionales**
· La secuencia permitida es: Registrado -> Asignado -> En progreso -> Resuelto -> Cerrado.
· El sistema impide retrocesos de estado (ej. de Resuelto a En progreso).

**No Funcionales**
· Registro automático en el historial de cambios ante cada transición.

**Priorización:** Media

---
### 5. Historia de usuario: Reasignación de Incidentes

**Requerimiento funcional y no funcional**
Como coordinador, quiero reasignar un incidente a otro técnico, para optimizar los tiempos de atención.

**Criterios de Aceptación Funcionales**
· El técnico anterior libera el incidente.
· El nuevo técnico debe cumplir con la especialidad y el límite de carga (3 incidentes activos).

**No Funcionales**
· Consistencia de datos al cambiar el técnico responsable.

**Priorización:** Media

---
### 6. Historia de usuario: Escalamiento Automático de Incidentes Críticos

**Requerimiento funcional y no funcional**
Como sistema, quiero marcar automáticamente un incidente como 'Escalado' si lleva más de 2 horas sin ser atendido, para evitar incumplimientos de SLA.

**Criterios de Aceptación Funcionales**
· Si el estado sigue en 'Registrado' después de 2 horas desde la creación, se marca como 'Escalado'.
· Se registra este evento en el historial.

**No Funcionales**
· Proceso en segundo plano (background worker) para monitoreo de tiempos.

**Priorización:** Alta

---
### 7. Historia de usuario: Validación de Especialidad Técnica

**Requerimiento funcional y no funcional**
Como sistema, quiero validar que el técnico asignado tenga la especialidad técnica coincidente con el tipo de incidente, para asegurar la capacidad de resolución.

**Criterios de Aceptación Funcionales**
· El sistema compara la especialidad del técnico vs el tipo de red (fibra, microondas, etc.) afectada.

**No Funcionales**
· Mapeo eficiente de especialidades técnicas.

**Priorización:** Alta

---
### 8. Historia de usuario: Historial de Cambios de Estado

**Requerimiento funcional y no funcional**
Como auditor, quiero visualizar el historial de cambios de estado de un incidente, para conocer la trazabilidad del proceso.

**Criterios de Aceptación Funcionales**
· Cada cambio de estado (fecha, hora, usuario, estado anterior, estado nuevo) debe ser persistido.

**No Funcionales**
· Historial inmutable; no debe ser modificable.

**Priorización:** Media

---
### 9. Historia de usuario: Generación de Reportes de Incidentes

**Requerimiento funcional y no funcional**
Como gerente, quiero obtener un reporte de los incidentes mensuales, para evaluar el cumplimiento de los SLA.

**Criterios de Aceptación Funcionales**
· Endpoint para listar incidentes filtrados por mes/año.
· Resumen de tiempos promedio de resolución.

**No Funcionales**
· Exportación eficiente a formatos legibles.

**Priorización:** Media

---
### 10. Historia de usuario: Visualización de Incidentes (Dashboard)

**Requerimiento funcional y no funcional**
Como técnico, quiero ver la lista de mis incidentes activos, para organizar mi jornada laboral.

**Criterios de Aceptación Funcionales**
· Filtro para ver solo incidentes asignados al usuario autenticado.

**No Funcionales**
· Interfaz de usuario rápida y responsiva.

**Priorización:** Baja

---
