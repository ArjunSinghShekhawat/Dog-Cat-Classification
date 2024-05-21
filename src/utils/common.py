import os
from pathlib import Path
import yaml
import joblib
import json
import sys
import base64
from box import ConfigBox
from typing import Any
from src.logger import logging
from src.exception import CustomeException
from ensure import ensure_annotations


@ensure_annotations
def read_yaml(filepath:Path)->ConfigBox:

    """This function is used to read yaml file"""
    try:
        with open(filepath) as file_obj:
            content = yaml.safe_load(file_obj)

            logging.info(f"file {filepath} yaml successfully read :")

        return ConfigBox(content)
    
    except Exception as e:
        raise CustomeException(e,sys)


@ensure_annotations
def create_directories(file_dir_list:list,verbose=True):
    """This function create directories"""

    for filedir in file_dir_list:
        os.makedirs(filedir,exist_ok=True)

        if verbose:
            logging.info(f"Filedur {filedir} Successfully Created :")


@ensure_annotations
def get_size(filepath:Path)->str:
    """This funcion is used for given the size of the file"""

    return os.path.getsize(filepath)


@ensure_annotations
def save_json(filepath:Path,data:dict):
    """This function is used to save json file"""

    with open(filepath,'w') as file_obj:
        json.dump(data,file_obj,indent=4)
        logging.info(f"Json file {filepath} Successfully save :")


@ensure_annotations
def load_json(filepath:Path)->ConfigBox:
    """This function is used to load json file """

    with open(filepath) as file_obj:
        content = json.load(file_obj)

        logging.info(f"Json file {filepath} Successfully Load")
        return ConfigBox(content)

@ensure_annotations
def save_bin(filepath:Path,data:Any):
    """This function is used to save binary file"""

    joblib.dump(data,filename=filepath)
    logging.info(f"Bnary file {filepath} Successfully save")


@ensure_annotations
def load_bin(filepath:Path)->Any:
    """This function is used to load binary file"""

    content = joblib.load(filepath)
    logging.info(f"Binary file {filepath} Successfully load")

    return content

@ensure_annotations 
def image_decoding(imageString:str,filepath:Path):
    """This function used for decode image"""

    image = base64.b64decode(imageString)

    with open(filepath,'wb') as file_obj:
        file_obj.write(image)
        file_obj.close()

@ensure_annotations
def image_encoding(filepath:Path):
    """This function is used for encoding image"""

    with open(filepath,'rb') as file_obj:
        return base64.b64encode(file_obj.read())





        
