# import os
# import sys
# import logging
# from src.cheese.utils.common import read_yaml
# from src.cheese.constants import *

# config = read_yaml(CONFIG_FILE_PATH)

# log_dir = "logs"
# log_filepath = os.path.join(log_dir, config['logging']['log_file'])
# os.makedirs(log_dir, exist_ok=True)

# logging.basicConfig(
#     level= logging.INFO,
#     format= config['logging']['format'],
#     datefmt=config['logging']['datefmt'],

#     handlers=[
#         logging.FileHandler(log_filepath),
#         logging.StreamHandler(sys.stdout)
#     ]
# )