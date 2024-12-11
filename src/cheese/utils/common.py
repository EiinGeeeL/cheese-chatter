import yaml
import os
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
    
def load_and_clean_text_file(file_path: str, remove_empty_lines: bool = False) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            if remove_empty_lines:
                content = "\n".join(line.strip() for line in file if line.strip())
            else:
                content = file.read().strip()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"Not found the file <{file_path}>.")
    
def save_text_to_artifact(content: str, filename: str = None) -> None:
    # Get the current working directory
    current_dir = os.getcwd()

    # Create 'artifacts' directory if it doesn't exist
    artifacts_dir = 'artifacts'
    os.makedirs(artifacts_dir, exist_ok=True)
    
    # Generate a filename if not provided
    if filename is None:
        # Use only the last part of the directory path
        safe_dir_name = current_dir.split('\\')[-1].replace(' ', '_')
        filename = f"artifact_{safe_dir_name}.txt"
    else:
        # Ensure the filename ends with .txt
        if not filename.endswith('.txt'):
            filename += '.txt'

    # Create the full file path
    file_path = os.path.join(artifacts_dir, filename)

    # Save the string to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
