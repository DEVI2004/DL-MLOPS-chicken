import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")
#above is a logging module which is specified in a format -with asci time and message --- it will generate the logs

project_name = "chickendisease"
#naming the project

list_of_files = [
    ".github/workflows/.gitkeep", #for github actions and workflows
    f"src/{project_name}/__init__.py", #constructor file_to import if needed
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml", #mlops tool
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"
]


#looping through each file
for filepath in list_of_files:
    filepath = Path(filepath) 
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
        #A log message is recorded for directory creation.
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filename}")

#the script logs every step using the logging module

#This script is useful for project setup automation, 
# ensuring that all required directories and files exist before development begins. 
# It is particularly useful in MLOps, software projects, and Python package development.