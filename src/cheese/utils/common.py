import yaml
from pathlib import Path
from typing import Dict, Optional

def read_yaml(path_to_yaml: Path) -> Optional[Dict]:
    """
    Read and parse a YAML file.

    Args:
        path_to_yaml (Path): A Path object representing the location of the YAML file.

    Returns:
        Optional[Dict]: A dictionary containing the parsed YAML data if successful,
                        or None if the file is empty or contains invalid YAML.

    Raises:
        FileNotFoundError: If the specified YAML file doesn't exist or isn't accessible.
        yaml.YAMLError: If there's an error parsing the YAML content.
        Exception: For any other unexpected errors.
    """

    try:
        with open(path_to_yaml, 'r') as yaml_file:
            yaml_content = yaml.safe_load(yaml_file)
            return yaml_content
    except FileNotFoundError:
        raise FileNotFoundError(f"The configuration file '{path_to_yaml}' does not exist.")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML file {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred {e}")