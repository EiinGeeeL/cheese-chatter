from langchain_ollama import ChatOllama, OllamaEmbeddings
from cheese.constants import *
from cheese.utils.common import read_yaml

class LLMServices:
    config = read_yaml(CONFIG_FILE_PATH)

    model = ChatOllama(
        model=config['ollama']['model'],
        temperature=config['ollama']['temperature'],
        # Add other parameters from config as needed
    )

    embeddings = OllamaEmbeddings(
        model=config['ollama']['embeddings'],
    )

    # quick_model = config['ollama']['quick_model']

    #multimodal = config['ollama']['multimodal']

    @classmethod
    def reinitialize(cls):
        cls.config = read_yaml(CONFIG_FILE_PATH)
        cls.model = ChatOllama(
            model=cls.config['ollama']['model'],
            temperature=cls.config['ollama']['temperature'],
            # Add other parameters from config as needed
        )
        cls.embeddings = OllamaEmbeddings(
            model=cls.config['ollama']['embeddings'],
        )