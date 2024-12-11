from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_openai import AzureChatOpenAI
from langchain_core.runnables import Runnable
from cheese.constants import *
from cheese.utils.common import read_yaml

class LLMServices:
    config = read_yaml(CONFIG_FILE_PATH)
    
    # Model available
    models_dict = {
        'ollama': ChatOllama(
            model=config['ollama']['model'],
            temperature=config['ollama']['temperature'],
            # Add other parameters from config as needed
        ),
        'azureopenai': AzureChatOpenAI( # Configured from .env
            temperature=config['azureopenai']['temperature'],
        ),
    }

    # Embeddings available
    embeddings_dict = {
        'ollama': OllamaEmbeddings(
            model=config['ollama']['embeddings'],
        ),
    }

    # Turbo model available
    turbo_models_dict = None

    model: Runnable = models_dict[config['launch']['model']]
    embeddings: Runnable = embeddings_dict[config['launch']['embeddings']]
    turbo_model: Runnable = turbo_models_dict

    @classmethod
    def reinitialize(cls):
        cls.config = read_yaml(CONFIG_FILE_PATH)
        
        # Reinitialize models_dict
        cls.models_dict = {
            'ollama': ChatOllama(
                model=cls.config['ollama']['model'],
                temperature=cls.config['ollama']['temperature'],
                # Add other parameters from config as needed
            ),
            'azureopenai': AzureChatOpenAI( # Configured from .env
                temperature=cls.config['azureopenai']['temperature'],
            ),
        }
        
        # Reinitialize embeddings_dict
        cls.embeddings_dict = {
            'ollama': OllamaEmbeddings(
                model=cls.config['ollama']['embeddings'],
            ),
        }
        
        # Reinitialize turbo_models_dict
        
        # Update model, embeddings, and turbo_model
        cls.model = cls.models_dict[cls.config['launch']['model']]
        cls.embeddings = cls.embeddings_dict[cls.config['launch']['embeddings']]
        cls.turbo_model = cls.turbo_models_dict.get(cls.config['launch']['turbo_model'])
