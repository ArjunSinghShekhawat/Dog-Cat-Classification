import os
from src.entity.config_entity import DataIngestionConfig
import urllib.request as request
from src.logger import logging
from pathlib import Path
import zipfile

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self):

        if (not os.path.exists(self.config.local_data_file)):
            filename,header = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logging.info(f"File download {filename} with info : {header}")
        
        else:
            logging.info(f"File already exists of size : {os.path.getsize(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir

        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)




            