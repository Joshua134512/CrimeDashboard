import pandas as pd
from config import settings
from os import path,curdir
import requests
from connectors.SQL import Database

ROOT = path.abspath(curdir)


#This class is used for accessing urls or files and returning data frames or raw data.
class Extractor:
    def __init__(self, source: str):
        self.source = source

    def __enter__(self):
        #Init
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value:
            print(exc_value)
    
    def get_data(self) -> pd.DataFrame:
        #Reads from file, returns data frame
        data = pd.read_json(self.source)
        return data
    
    def get_file(self) -> bytes:
        #Reads from url or path, returns bytes
        if isinstance(self.source, str):
            response = requests.get(self.source)
            rtn = response.content
        else:
            with open(self.source, 'rb') as f:
                rtn = f.read()
        return rtn
    
    def to_sql(self, table, database):
        df = self.get_data()
        with Database(database) as db:
            db.table_from_dataframe(df, table)