import pandas as pd
from config import settings
from os import path,curdir

ROOT = path.abspath(curdir)


class Extractor:
    def __init__(self, city: str, file: None|str):
        self.url = settings.data[city]['url']
        if  file:
            self.file = open(file, 'w')
        else: 
            ext = 'data/' + city + '.csv'
            self.file = open(path.join(ROOT, ext),'w')

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_value:
            print(exc_value)
    
    def downloadData(self) -> pd.DataFrame:
        data = pd.read_csv(self.url)
        return data
    
    def writeToFile(self):
        data = self.downloadData()
        self.file.write(data.to_csv())

