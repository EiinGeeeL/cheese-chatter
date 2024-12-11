# Cheese-Chatter
Cheese Chatter es una app LLM preparada para integrarse en un bot de Telegram. 
La aplicación construida en langchain-langgraph-langserver tiene la siguiente arquitectura:

![alt text](/artifacts/cheese_graph.png)

## Requisitos previos

- Python 3.12.5
- Ollama 4.0 o superior; o .env configurada para Azure AI Deployment
- pip (gestor de paquetes de Python)

## Instalación

1. Clona el repositorio:

(preguntar a un administrador)

2. Crea un entorno virtual:

```py -m venv .venv```

3. Activa el entorno virtual:
- En Windows:
  ```.venv\Scripts\activate```
- En macOS y Linux:
  ```source .venv/bin/activate```

4. Instala las dependencias:

```pip install -r requirements.txt```


## Ejecución

Para ejecutar el proyecto:

1. Ejecutar el servicio Ollama (en caso de modelo en local)

```ollama run llama3.1```

2. Ejecutar la app LangServer

```py main.py```


## Estructura del repositorio

```bash
cheese-chatter/
├── main.py                # Archivo principal para ejecutar el proyecto
├── app.py                 # Archivo principal para ensamblar la app
├── runnable.ipynb         # Notebook para debugear e interacturar con el proyecto
├── requirements.txt       # Lista de dependencias del proyecto
├── .env                   # Variables de entorno para la configuración
├── README.md              # Documentación del proyecto
├── src/
│   └── cheese/
│       ├── components/
│       │   ├── nodes/
│       │   ├── edges/
│       │   │   ├── evaluators/      # Contiene StateEvaluator para conditional edges
│       │   │   └── conditionals/    # Contiene ConditionalEdge
│       │   ├── tools/               # Contiene BaseTool
│       │   └──...
│       ├── utils/
│       │   ├── common.py
│       │   ├── logger.py
│       │   └── type_vars.py
│       ├── config/                  # Contiene scripts de configuración del LLMs
│       │   └── prompt/              # Contiene los prompts.txt de configuración
│       ├── managers/      # Contiene managers clases
│       ├── services/      # Contiene servicios
│       ├── entity/
│       │   ├── models/              # Contiene modelos de estructura
│       │   ├── node.py              # Contiene las entidades principales asociados a los nodos
│       │   └── edge.py              # Contiene las entidades principales asociados a los edge
│       └── constants/
│           └── __init__.py          # Contiene las constantes del proyecto
├── config/
│   └── config.yaml        # Archivos de configuración principal
├── research/              # Directorio para scripts y ipynb de experimentación
├── tests/                 # Directorio para módulos testing
│   ├── integration_test/
│   └── unit_test/
├── artifacts/             # Directorio para archivos
│   ├── cheese_graph.png   # Imagen de la arquitectura principal de la aplicación
│   └── models/            # Directorio para modelos generados en research
└── logs/                  # Directorio para logs del proyecto
```
