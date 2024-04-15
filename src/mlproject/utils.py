import os 
import sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql
load_dotenv()
host = os.getenv('host')
password  = os.getenv('password')
user = os.getenv('user')
db= os.getenv('db')

def read_sql_data():
    logging.info('Reading Database started')
    try:

        mydb = pymysql.connect(
        host = host, user = user, password = password, db = db
    )
        logging.info("Connection established with Database")
        df = pd.read_sql_query("select * from student", mydb)
    except Exception as ex:
        raise CustomException(ex, sys)
