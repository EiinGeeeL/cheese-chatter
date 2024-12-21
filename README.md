# Cheese-Chatter
Cheese Chatter is an LLM app ready to integrate with a Telegram bot.  
The application is built with langchain-langgraph-langserver and has the following architecture:

![alt text](/artifacts/cheese_graph.png)

## Prerequisites

- Python 3.12.5
- Ollama 4.0 or higher; or a .env file configured for Azure AI Deployment
- pip (Python package manager)

## Installation

1. Clone the repository:

2. Create a virtual environment:

```py -m venv .venv```

3. Activate the virtual environment:
- On Windows:
  ```.venv\Scripts\activate```
- On macOS and Linux:
  ```source .venv/bin/activate```

4. Install the dependencies:

```pip install -r requirements.txt```


## Running the Project

To run the project:

1. Start the Ollama service (if using a local model)

```ollama run llama3.1```

2. Run the LangServer app

```py main.py```


## Repository Structure

```bash
cheese-chatter/
├── main.py                # Main file to run the project
├── app.py                 # Main file to assemble the app
├── runnable.ipynb         # Notebook for debugging and interacting with the project
├── requirements.txt       # Project dependency list
├── .env                   # Environment variables for configuration
├── README.md              # Project documentation
├── src/
│   └── cheese/
│       ├── components/
│       │   ├── nodes/
│       │   ├── edges/
│       │   │   ├── evaluators/      # Contains StateEvaluator for conditional edges
│       │   │   └── conditionals/    # Contains ConditionalEdge
│       │   ├── tools/               # Contains BaseTool
│       │   └── runnables/           # Contains executable invoke files
│       ├── utils/
│       │   ├── common.py
│       │   ├── logger.py
│       │   └── type_vars.py
│       ├── config/                 
│       │   ├── config_graph.py      # Contains the definition of graph nodes and edges
│       │   └── runnables/           # Contains prompts and LLM configuration
│       ├── managers/      # Contains manager classes
│       ├── services/      # Contains services
│       ├── entity/
│       │   ├── models/              # Contains structural models
│       │   ├── node.py              # Contains main entities related to nodes
│       │   └── edge.py              # Contains main entities related to edges
│       └── constants/
│           └── __init__.py          # Contains project constants
├── config/
│   └── config.yaml        # Main configuration files
├── research/              # Directory for experimentation scripts and notebooks
├── tests/                 # Directory for testing modules
│   ├── integration_test/
│   └── unit_test/
├── artifacts/             # Directory for artifacts
│   ├── cheese_graph.png   # Image of the application's main architecture
│   └── models/            # Directory for models generated in research
└── logs/                  # Directory for project logs
