import setuptools
from src.cheese.constants import *

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open(CONFIG_FILE_PATH, 'r') as f:
    config = {}
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            if line.endswith(':'):
                current_section = line[:-1].strip()
                config[current_section] = {}
            else:
                key, _, value = line.partition(':')
                key = key.strip()
                value = value.strip().strip("'\"")
                config.setdefault(current_section, {})[key] = value

__version__ = config['package']['version']

REPO_NAME = config['package']['repo_name']
AUTHOR_USER_NAME = config['package']['author_user_name']
SRC_REPO = config['package']['src_repo']
AUTHOR_EMAIL = config['package']['author_email']
DESCRIPTION = config['package']['description']

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    setup_requires=['PyYAML'],
    install_requires=['PyYAML'],
)