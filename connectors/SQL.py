import sqlite3
import pandas as pd

class Database:
    def __init__(self, database: str):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.commit()
        self.connection.close()
        return exc_value
    
    def execute_sql(self, sql):
        return self.cursor.execute(sql)
    
    def table_from_dataframe(self, dataframe: pd.DataFrame, table):
        print(dataframe.to_sql(table, self.connection))

    def insert_row(self, columns, row, table):
        sql = f"insert into {table} ({columns}) values({row})"
        print(sql)
        self.execute_sql(sql)
