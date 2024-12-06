from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.runnables import Runnable
from cheese.constants import *
from cheese.utils.common import read_yaml

class LLMServices:
    config = read_yaml(CONFIG_FILE_PATH)

    model: Runnable = ChatOllama(
        model=config['ollama']['model'],
        temperature=config['ollama']['temperature'],
        # Add other parameters from config as needed
    )

    embeddings = OllamaEmbeddings(
        model=config['ollama']['embeddings'],
    )

    # turbo_model = config['ollama']['turbo_model']

    # multimodal = config['ollama']['multimodal']

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