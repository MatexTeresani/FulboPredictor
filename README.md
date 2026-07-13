# ⚽ Match Predictor

Proyecto de predicción de resultados de partidos de fútbol utilizando Machine Learning e Inteligencia Artificial.

## Objetivo

Construir un pipeline completo que permita:

* Obtener datos históricos de partidos.
* Limpiar y procesar los datos.
* Generar variables predictivas (Feature Engineering).
* Entrenar modelos de Machine Learning.
* Evaluar su rendimiento.
* Exponer el modelo mediante una API para realizar predicciones.

---

# Stack tecnológico

* Python 3.11
* Pandas
* NumPy
* Scikit-Learn
* LightGBM
* CatBoost
* Optuna
* FastAPI
* Jupyter

---

# Estructura del proyecto

```text
src/
│
├── api/
├── config/
├── data/
├── features/
├── models/
└── utils/

data/
├── raw/
├── processed/
└── external/

models/
tests/
notebooks/
```

---

# Primeros pasos

## 1. Clonar el repositorio

```bash
git clone <repo>
cd match-predictor
```

## 2. Crear el entorno virtual

Windows

```bash
py -3.11 -m venv .venv
```

Linux

```bash
python3.11 -m venv .venv
```

## 3. Activarlo

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Flujo de trabajo

```
Datos
    ↓
Limpieza
    ↓
Feature Engineering
    ↓
Entrenamiento
    ↓
Evaluación
    ↓
Optimización
    ↓
Predicción
```

---

# Distribución inicial de tareas

## Integrante 1 — Obtención de datos

Responsabilidades:

* Descargar datasets históricos.
* Integrar Football-Data.
* Integrar API-Football.
* Guardar datos en `data/raw`.

Archivos:

```
src/data/downloader.py
src/data/loader.py
```

---

## Integrante 2 — Limpieza y procesamiento

Responsabilidades:

* Normalizar nombres de equipos.
* Eliminar datos inconsistentes.
* Manejar valores faltantes.
* Crear dataset limpio.

Archivos:

```
src/data/preprocessing.py
```

---

## Integrante 3 — Ingeniería de características

Responsabilidades:

* Elo Rating.
* Forma de los últimos partidos.
* Estadísticas acumuladas.
* Local vs visitante.
* Historial entre equipos.

Archivos:

```
src/features/
```

---

## Integrante 4 — Machine Learning

Responsabilidades:

* Baseline.
* LightGBM.
* CatBoost.
* Optimización con Optuna.
* Guardado del modelo.

Archivos:

```
src/models/
```

---

## Integrante 5 — API

Responsabilidades:

* Endpoint de predicción.
* Carga del modelo.
* Validación de entrada.
* Documentación automática.

Archivos:

```
src/api/
```

---

# Convenciones

* Código en inglés.
* Variables descriptivas.
* Funciones pequeñas y reutilizables.
* Cada cambio mediante Pull Request.
* No subir datasets grandes ni modelos entrenados al repositorio.

---

# Roadmap

## Fase 1

* [ ] Descargar datos históricos.
* [ ] Crear pipeline de limpieza.
* [ ] Construir dataset final.

## Fase 2

* [ ] Implementar Feature Engineering.
* [ ] Entrenar modelo base.
* [ ] Evaluar métricas.

## Fase 3

* [ ] Optimizar hiperparámetros.
* [ ] Comparar modelos.
* [ ] Seleccionar el mejor.

## Fase 4

* [ ] Crear API.
* [ ] Realizar pruebas.
* [ ] Desplegar el modelo.

---

# Objetivo final

Desarrollar un sistema reproducible capaz de estimar probabilidades de victoria, empate o derrota utilizando datos históricos y técnicas modernas de Machine Learning.
