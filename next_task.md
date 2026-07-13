Próxima tarea inmediata

La siguiente pieza de infraestructura con mayor impacto es la configuración centralizada del proyecto.

Commit futuro:

feat: add centralized project settings

Objetivo:

Crear src/config/settings.py para centralizar todas las rutas y configuraciones compartidas.

Debería definir, como mínimo:

ROOT_DIR
DATA_DIR
RAW_DATA_DIR
INTERIM_DATA_DIR
PROCESSED_DATA_DIR
ARTIFACTS_DIR
LOGS_DIR

Y, si van a usar variables de entorno:

Cargar .env con python-dotenv.
Definir configuraciones como la API Key de API-Football.

La idea es que ningún módulo del proyecto vuelva a escribir rutas como:

"../../data/raw"

o

"C:/Users/..."

Todo debe obtenerse desde settings.py, lo que facilita mover el proyecto entre máquinas y mantener una única fuente de configuración.