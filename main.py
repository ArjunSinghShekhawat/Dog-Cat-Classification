from src.pipeline.stage_data_ingestion_pipeline import DataIngestionTraningPipeline
from src.logger import logging
from src.exception import CustomeException
import  sys

STATE_NAME  = "Data Ingestion"

if __name__=="__main__":

    try:
        logging.info("Started")
        logging.info(f">>>>>>>>>>{STATE_NAME}>>>>>>>>>")    
        obj = DataIngestionTraningPipeline()
        obj.main()
        logging.info("Ending")
        logging.info(f">>>>>>>>>>>{STATE_NAME}>>>>>>>>>>")
        
    except Exception as e:
        raise CustomeException(e,sys)