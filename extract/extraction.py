import pandas as pd
from config import settings
from os import path,curdir

ROOT = path.abspath(curdir)

#TODO add option to read from path, download csv directly
class Extractor:
    def __init__(self, url: str):
        self.url = url

    def __enter__(self):
        #Init
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value:
            print(exc_value)
    
    def download_data(self) -> pd.DataFrame:
        #Reads from url, returns data frame
        data = pd.read_csv(self.url)
        return data
    
    def download_csv(self) -> str:
        #Reads from url, returns csv string
        data = self.downloadData()
        return data.to_csv()

