import sqlite3

class Database:
    def __init__(self, database: str):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()
        return exc_value
    
    def execute_sql(self, sql):
        self.cursor.execute(sql)
