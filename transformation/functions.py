from connectors.SQL import Database
from os import path,curdir
import pandas as pd

ROOT = path.abspath(curdir)

def execute_sql_from_file(file: str, database = "test.db", **_):
    filepath = path.join(ROOT, 'transformation', 'resources', file)
    with open(filepath, 'r') as f:
        sql = f.read()
    execute_sql(sql, database)
    return

def execute_sql(sql: str, database = "test.db", **_):
    with Database(database) as db:
        db.execute_sql(sql)
    return

def execute_custom_sql(database = "test.db", **_):
    with Database(database) as db:
        while True:
            userIn = input("Enter script or type exit to end program: ")
            if(userIn == "exit"):
                break
            else:
                try: 
                    results = db.execute_sql(userIn)
                    print(results.fetchall())
                except:
                    print("SQL Error")

def table_from_csv(file, database = "test.db", table = "test", header = None, **_):
    filepath = path.join(ROOT, 'data', 'working', file)
    with open(filepath, 'r') as f:
        data = f.read()
    with Database(database) as db:
        lines = data.splitlines()
        for row in lines:
            row = row.strip()
            if not header:
                header = row
                sql = f"create table if not exists {table} ({header})"
                db.execute_sql(sql)
            else:
                fRow = ""
                for item in row.split(','):
                    fRow += f"'{item.strip()}',"  
                db.insert_row(header, fRow[:-1], table)


def retrieve_raw_data(file, **_):
    source = path.join(ROOT, "data", "rawdata", file)
    target = path.join(ROOT, "data" ,"working", file)
    with open(source, 'rb') as f:
        data = f.read()
    with open(target, 'wb') as f:
        f.write(data)

def table_to_file(file, database = "test.db", table = "test", **_):
    sql = f"select * from {table}"
    with Database(database) as db:
        data = pd.read_sql_query(sql, db.connection)
        filepath = path.join(ROOT, 'data', 'output', file)
        data.to_csv(filepath)
        