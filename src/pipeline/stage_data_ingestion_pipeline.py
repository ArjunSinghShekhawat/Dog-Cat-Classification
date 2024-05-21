from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.exception import CustomeException
import sys

class DataIngestionTraningPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
           config = ConfigurationManager()
           data_ingestion_config = config.get_data_ingestion_config()
           data_ingestion = DataIngestion(data_ingestion_config)
           data_ingestion.download_file()
           data_ingestion.extract_zip_file()
        except Exception as e:
           raise CustomeException(e,sys)
