# ADR-003: Almacenamiento y ejecución

## Estado
Aceptada.

## Contexto
El proyecto debe poder ejecutarse y evaluarse desde GitHub.

## Alternativas
- Almacenamiento local de datos y resultados.
- Base de datos externa.
- Servicio de almacenamiento en la nube.

## Decisión
Mantener una copia del dataset en data/raw y generar
los resultados en reports mediante scripts de Python.

## Justificación
El volumen de datos es pequeño y no justifica una base
de datos ni una infraestructura de despliegue adicional.
Se documentará la fuente original y el proceso de descarga.