# ADR-002: Selección del modelo de clasificación

## Estado
Aceptada.

## Contexto
Se requiere un modelo básico y explicable.

## Alternativas
- Árbol de decisión.
- K vecinos más cercanos (KNN).
- Regresión logística.

## Decisión
Utilizar un árbol de decisión como modelo principal
y DummyClassifier como referencia.

## Justificación
El árbol permite explicar las reglas de clasificación y
comparar su desempeño con una estrategia de referencia.