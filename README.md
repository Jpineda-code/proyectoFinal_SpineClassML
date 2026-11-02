# SpineClass ML: clasificación de datos biomecánicos

## 1. Descripción del proyecto

SpineClass ML es un proyecto educativo de Machine Learning que utiliza un árbol de decisión para clasificar observaciones de un conjunto de datos biomecánicos de la columna vertebral. El objetivo es evaluar el desempeño del modelo mediante métricas cuantitativas y analizar sus limitaciones técnicas y éticas.

## 2. Objetivo

Implementar un modelo básico de clasificación, compararlo con un modelo de referencia y evaluar sus resultados mediante métricas de clasificación y una matriz de confusión.

## 3. Alcance del sistema

### Qué hará
- Cargar y validar un dataset público.
- Explorar las variables y la distribución de las clases.
- Entrenar un árbol de decisión y un modelo de referencia.
- Calcular métricas de evaluación.
- Generar tablas y gráficas de resultados.
- Documentar los riesgos y las consideraciones éticas.

### Qué no hará
- Diagnosticar pacientes reales.
- Recomendar tratamientos médicos.
- Sustituir la valoración de un profesional de la salud.
- Garantizar resultados válidos para poblaciones diferentes a las representadas en el dataset.

## 4. Dataset

Fuente: UCI Machine Learning Repository.

Dataset: Vertebral Column.

URL: https://archive.ics.uci.edu/dataset/212/vertebral+column

El conjunto de datos contiene 310 observaciones, seis variables biomecánicas y una variable de clase. Se utilizarán las tres categorías disponibles en la tarea de clasificación multiclase.

## 5. Tecnologías

- Python
- pandas y NumPy
- scikit-learn
- Matplotlib y Seaborn
- Jupyter Notebook
- Git y GitHub
- pytest y GitHub Actions

## 6. Arquitectura

Consultar el diagrama C4 de contexto en `docs/arquitectura.md`.

Las decisiones de arquitectura se documentan en `docs/adr/`.

## 7. Metodología

1. Obtener y validar los datos.
2. Analizar las variables y la distribución de las clases.
3. Separar los datos en entrenamiento y prueba.
4. Entrenar el modelo de referencia.
5. Entrenar el árbol de decisión.
6. Calcular las métricas en el conjunto de prueba.
7. Comparar los resultados e interpretar los errores.
8. Documentar las conclusiones técnicas y éticas.

La separación se realiza de manera estratificada, con una proporción de 80 % para entrenamiento y 20 % para prueba, utilizando una semilla fija para favorecer la reproducibilidad.

## 8. Evaluación

Se utilizarán las siguientes métricas:

- Accuracy.
- Precision macro.
- Recall macro.
- F1-score macro.
- Matriz de confusión.
- Comparación con el modelo de referencia.

Los resultados reales se almacenarán en `reports/metrics.csv` y `reports/classification_report.csv`. La matriz de confusión se generará en `reports/figures/confusion_matrix.png`.

La aceptación del modelo se evaluará utilizando los siguientes criterios. Los resultados no se considerarán satisfactorios únicamente por obtener un accuracy elevado.

| Criterio | Umbral propuesto |
|---|---|
| F1-score macro del árbol | ≥ 0,10 puntos absolutos por encima del baseline |
| Recall de cada clase | ≥ 0,50 |
| Reproducibilidad | Mismos resultados con los mismos datos y parámetros |

En los resultados actuales, el árbol supera al baseline en F1-score macro (0,665 frente a 0,217), pero la condición de recall por clase no se cumple, ya que la clase Normal alcanza 0,40 frente al umbral de 0,50.

## 9. Riesgos técnicos

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Dataset limitado | Generalización restringida | Documentar la representatividad y las limitaciones |
| Fuga de información | Métricas artificialmente elevadas | Separar los datos antes de entrenar |
| Sobreajuste | Bajo rendimiento con datos nuevos | Controlar la complejidad y evaluar en datos de prueba |
| Sesgos | Errores potencialmente desiguales | Analizar las métricas por clase y documentar limitaciones |
| Problemas de reproducibilidad | Dificultad para repetir el experimento | Registrar dependencias, parámetros y procedimientos |

## 10. Análisis ético

El modelo se utilizará exclusivamente con fines educativos. Se documentarán los posibles sesgos, la representatividad del dataset, la privacidad, los riesgos de interpretación y las limitaciones de su aplicación en contextos de salud.

Consultar el análisis completo en `docs/analisis_etico.md`.

## 11. Instalación y ejecución

Crear un entorno virtual e instalar las dependencias:

```bash
python -m venv .venv
pip install -r requirements.txt
```

Descargar el dataset:

```bash
python -m src.download_data
```

Entrenar y evaluar los modelos:

```bash
python -m src.train_model
python -m src.evaluate_model
```

Ejecutar las pruebas:

```bash
python -m pytest -v
```

Para revisar el análisis exploratorio, abrir `notebook/01_exploracion_y_modelado.ipynb` en Jupyter o Visual Studio Code.

## 12. Estructura del repositorio

- `data/`: datos originales y datos procesados.
- `notebooks/`: análisis exploratorio y demostración.
- `src/`: código Python del experimento.
- `tests/`: pruebas automáticas.
- `docs/`: arquitectura, ADR y análisis ético.
- `reports/`: métricas y gráficas generadas.

## 13. Glosario

- **Accuracy:** proporción de predicciones correctas.
- **Precision:** proporción de predicciones positivas correctas para una clase.
- **Recall:** proporción de casos reales de una clase que fueron identificados.
- **F1-score:** media armónica entre precision y recall.
- **Baseline:** modelo de referencia utilizado para comparar resultados.
- **Sobreajuste:** situación en la que un modelo aprende demasiado los datos de entrenamiento y no generaliza adecuadamente.
- **Data leakage:** uso indebido de información que no debería estar disponible durante el entrenamiento.

## 14. Conclusiones

En el experimento realizado, el árbol de decisión obtuvo un accuracy de 0.726 y un F1-score macro de 0.665, superando al modelo de referencia, cuyo F1-score macro fue de 0.217. La diferencia evidencia una mejora en la clasificación de las tres categorías del conjunto de prueba.

Sin embargo, el desempeño fue desigual entre clases. El modelo identificó correctamente 28 de 30 observaciones de Spondylolisthesis, 9 de 12 de Hernia y 8 de 20 de Normal. La clase Normal presentó la mayor cantidad de errores, por lo que el accuracy global no describe por sí solo el comportamiento del clasificador.

Los resultados corresponden a una evaluación educativa sobre un conjunto de datos público y una partición específica de entrenamiento y prueba. No permiten concluir que el modelo sea adecuado para diagnosticar pacientes ni que generalice a otras poblaciones. Como trabajo futuro, se recomienda ampliar la evaluación con validación cruzada, revisar los errores por clase y estudiar la representatividad de los datos.

## 15. Referencias

Barreto, G., & Neto, A. (2005). *Vertebral Column* [Conjunto de datos]. UCI Machine Learning Repository. https://doi.org/10.24432/C5K89C.

Scikit-learn. (s. f.). *scikit-learn: Machine learning in Python*. https://scikit-learn.org/

Python Software Foundation. (s. f.). *Python documentation*. https://docs.python.org/3/

GitHub. (s. f.). *GitHub Actions documentation*. https://docs.github.com/actions
