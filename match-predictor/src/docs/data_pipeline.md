# ⚽ Match Predictor

Sistema de predicción de resultados de partidos de fútbol utilizando Machine Learning.

Actualmente el proyecto se encuentra en la fase de **preparación y normalización de datos**, construyendo una base sólida para futuras etapas de Feature Engineering y entrenamiento de modelos.

---

# Arquitectura actual

El flujo principal del sistema es:

```
data/raw/
    |
    v
Loader
    |
    v
Schema Normalization
    |
    v
Dataset Identity
    |
    v
Preprocessing
    |
    v
data/processed/
```

El objetivo de esta etapa es convertir datasets externos con estructuras diferentes en datasets internos consistentes.

---

# Flujo completo

## 1. Raw Data

Ubicación:

```
data/raw/
```

Contiene los datasets originales descargados de fuentes externas.

Ejemplos:

```
data/raw/
├── ARG.csv
├── E0.csv
├── E1.csv
├── E2.csv
└── ...
```

Estos archivos pueden tener diferentes nombres de columnas dependiendo del proveedor.

Ejemplo:

Football-Data:

```csv
Div,Date,HomeTeam,AwayTeam,FTHG,FTAG,FTR
```

Otro proveedor:

```csv
League,Date,Home,Away,HG,AG,Res
```

El sistema no trabaja directamente con estos formatos.

---

# Data Pipeline

Ubicación:

```
src/pipelines/data_pipeline.py
```

Es el encargado de coordinar todas las etapas de preparación.

Responsabilidad:

* Leer datasets disponibles.
* Normalizar columnas.
* Identificar el dataset.
* Aplicar limpieza.
* Guardar resultados procesados.

Flujo:

```python
df = load_csv(path)

df = normalize_schema(df)

identity = identify_dataset(df)

df = preprocess(df)

save_processed_dataset(df)
```

---

# Loader

Archivo:

```
src/data/loader.py
```

Responsabilidad:

Leer y escribir archivos.

No modifica datos.
No conoce reglas de fútbol.

---

## list_raw_datasets()

Busca automáticamente todos los CSV disponibles:

```python
data/raw/*.csv
```

Ejemplo:

Entrada:

```
data/raw/

ARG.csv
E0.csv
E1.csv
```

Salida:

```python
[
 "ARG.csv",
 "E0.csv",
 "E1.csv"
]
```

Esto evita depender de nombres manuales.

---

## load_csv()

Convierte un archivo CSV en un DataFrame de pandas.

Ejemplo:

```
ARG.csv
```

se convierte en:

```
pandas.DataFrame
```

---

## save_processed_dataset()

Guarda el resultado final en:

```
data/processed/
```

Ejemplo:

```
data/processed/ARG.csv
```

---

# Schema Normalization

Archivo:

```
src/data/normalize.py
```

Responsabilidad:

Convertir diferentes formatos externos a un esquema interno común.

---

## Problema

Diferentes fuentes utilizan diferentes nombres.

Ejemplo:

Fuente 1:

```text
HomeTeam
AwayTeam
FTHG
FTAG
FTR
```

Fuente 2:

```text
Home
Away
HG
AG
Res
```

Representan la misma información.

---

## Solución

Crear un esquema interno:

```text
competition
season
match_date
match_time

home_team
away_team

home_goals
away_goals

result
```

---

Ejemplo de transformación:

Antes:

```text
HomeTeam
```

Después:

```text
home_team
```

---

El sistema conserva columnas desconocidas.

Ejemplo:

Columnas de apuestas:

```
B365H
PSH
AvgH
```

no son eliminadas.

Esto permite utilizarlas posteriormente como posibles features.

---

# Dataset Identity

Archivo:

```
src/data/dataset_identity.py
```

Responsabilidad:

Obtener información sobre el dataset.

No modifica datos.

Genera metadata.

---

Ejemplo:

Entrada:

```
E0.csv
```

Resultado:

```python
DatasetIdentity(
    competition="E0",
    season="2025-2026",
    start_date="2025-08-01",
    end_date="2026-05-20",
    matches=380,
    features=124
)
```

---

Información obtenida:

## Competition

Competencia detectada.

Ejemplo:

```
Premier League
Liga Profesional
E0
```

---

## Season

Temporada calculada utilizando las fechas.

Ejemplo:

Fechas:

```
2025-08-01
2026-05-20
```

Resultado:

```
2025-2026
```

---

## Date Range

Permite conocer:

* primer partido del dataset.
* último partido.
* rango histórico disponible.

---

## Matches

Cantidad de partidos:

Ejemplo:

```
380 matches
```

---

## Features

Cantidad de columnas disponibles.

Ejemplo:

```
124 features
```

---

# Preprocessing

Archivo:

```
src/data/preprocessing.py
```

Responsabilidad:

Realizar limpieza básica del dataset.

Actualmente incluye:

---

## Remove duplicates

Elimina partidos duplicados.

Ejemplo:

Antes:

```
Barcelona - Real Madrid 2-1
Barcelona - Real Madrid 2-1
```

Después:

```
Barcelona - Real Madrid 2-1
```

---

## Drop empty rows

Elimina filas completamente vacías.

Ejemplo:

Antes:

```
E0 Arsenal Chelsea 2 1

NULL NULL NULL NULL
```

Después:

```
E0 Arsenal Chelsea 2 1
```

---

# Estado actual

Implementado:

* [x] Lectura automática de datasets.
* [x] Pipeline reproducible.
* [x] Normalización inicial de esquemas.
* [x] Identificación automática del dataset.
* [x] Limpieza básica.
* [x] Exportación a processed.

---

# Próximas etapas

## 1. Validación de datos

Crear:

```
src/data/validation.py
```

Responsabilidades:

* Verificar columnas necesarias.
* Detectar valores inválidos.
* Validar fechas.
* Validar goles.
* Detectar equipos faltantes.

---

## 2. Mejorar preprocessing

Agregar:

* Conversión de tipos.
* Normalización de nombres.
* Tratamiento de valores faltantes.
* Reglas específicas de fútbol.

---

## 3. Feature Engineering

Crear:

```
src/features/
```

Generar variables predictivas:

* Elo Rating.
* Forma reciente.
* Promedio de goles.
* Historial entre equipos.
* Rendimiento local/visitante.
* Días de descanso.

---

## 4. Model Training

Crear:

```
src/models/
```

Incluyendo:

* Baseline.
* LightGBM.
* CatBoost.
* Optimización con Optuna.
* Evaluación.

---

# Ejecución

Desde la raíz del proyecto:

```bash
python -m src.main
```

---

# Estructura actual

```
match-predictor/

├── data/
│   ├── raw/
│   └── processed/

├── src/
│   |
│   ├── data/
│   │   ├── loader.py
│   │   ├── normalize.py
│   │   ├── dataset_identity.py
│   │   └── preprocessing.py
│   |
│   ├── pipelines/
│   │   └── data_pipeline.py
│   |
│   ├── models/
│   |
│   ├── features/
│   |
│   └── utils/
│
├── notebooks/
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

# Principio de diseño

Cada módulo tiene una responsabilidad única:

| Módulo        | Responsabilidad             |
| ------------- | --------------------------- |
| loader        | Leer y guardar archivos     |
| normalize     | Convertir esquemas externos |
| identity      | Describir el dataset        |
| preprocessing | Limpiar datos               |
| pipeline      | Coordinar procesos          |

La idea es que nuevos datasets puedan agregarse sin modificar la arquitectura existente.
