```mermaid
flowchart LR
    U["Usuario / estudiante"]
    S["SpineClass ML<br/>Sistema de clasificación"]
    D["Dataset biomecánico<br/>UCI Repository"]
    R["Resultados<br/>Métricas y gráficas"]

    U -->|"Ejecuta el experimento"| S
    D -->|"Proporciona observaciones"| S
    S -->|"Genera evaluación"| R
    U -->|"Consulta resultados"| R
