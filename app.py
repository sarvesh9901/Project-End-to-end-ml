from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_injection import DataIngestion
from src.mlproject.components.data_injection import DataIngestionConfig
import sys
if __name__ == '__main__':
    logging.info('Running')
    try:
        #data_injection_config = DataInjectionConfig()
        data_injection = DataIngestion() 
        data_injection.initiate_data_ingestion()
    except Exception as e:
        logging.info("exception found")
        raise CustomException(e,sys)