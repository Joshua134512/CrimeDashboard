import sqlite3

class Database:
    def __init__(self, database: str):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_value, *_):
        self.connection.commit()
        self.connection.close()
        if exc_value:
            print(exc_value)
        return exc_value
    
    def execute_sql(self, sql):
        return self.cursor.execute(sql)

    def insert_row(self, columns, row, table):
        sql = f"insert into {table} ({columns}) values({row})"
        self.execute_sql(sql)