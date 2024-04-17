from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_injection import DataIngestion
from src.mlproject.components.data_injection import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformationConfig,DataTransformation
#from src.mlproject.components.model_tranier import ModelTrainerConfig,ModelTrainer
import sys
if __name__ == '__main__':
    logging.info('Running')
    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)
    except Exception as e:
        logging.info("exception found")
        raise CustomException(e,sys)