from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

file_list = [
    "src/__init__.py",
    "src/components/__init__.py",
    "src/constants/__init__.py",
    "src/utils/__init__.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/entity/__init__.py",
    "src/logger.py",
    "src/exception.py",
    "src/pipeline/__init__.py",
    "README.md",
    "main.py",
    "params.yaml",
    "config/config.yaml",
    "templates/index.html",
    "templates/home.html",
    ".gitignore",
]

for filepath in file_list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory {filedir} successfully created")
    
    full_path = Path(filedir) / filename
    if not full_path.exists() or full_path.stat().st_size == 0:
        with open(full_path, 'w') as file_obj:
            pass
        logging.info(f"File {full_path} successfully created")
    else:
        logging.info(f"File {full_path} already exists")
