from connectors.SQL import Database
from os import path,curdir
import pandas as pd

ROOT = path.abspath(curdir)
STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


def execute_sql_from_file(file: str, database = "test.db", **kwargs):
    filepath = path.join(ROOT, 'transformation', 'resources', file)
    with open(filepath, 'r') as f:
        sql = f.read()
    sql = sql.format(**kwargs)
    commands = sql.split(';')
    print(f"Executing sql file {file}")
    for command in commands:
        execute_sql(command, database)

def execute_sql(sql: str, database = "test.db", **_):
    with Database(database) as db:
        results = db.execute_sql(sql)
        print(results.fetchall())
    return

def execute_custom_sql(database = "test.db", **_):
    with Database(database) as db:
        while True:
            userIn = input("Enter script or type exit to end program: ")
            if(userIn == "exit"):
                break
            else:
                results = db.execute_sql(userIn)
                print(results.fetchall())


def json_to_table(folder, sql_file, database = "test.db", **kwargs):
    for state in STATES:
        kwargs['state'] = state
        file = state + '.json'
        filepath = path.join(ROOT, 'data', 'working', folder, file)
        with open(filepath, 'r') as f:
            data = f.read()
        kwargs['json'] = data
        execute_sql_from_file('stage_state.sql', database, **kwargs)
        execute_sql_from_file(sql_file, database, **kwargs)

def table_from_csv(file, database = "test.db", table = "test", **_):
    filepath = path.join(ROOT, 'data', 'working', file)
    df = pd.read_csv(filepath)
    print(f"Loading file {filepath} into table {table} in database {database}")
    with Database(database) as db:
        df.to_sql(table, db.connection)
    

def retrieve_raw_data(file, **_):
    source = path.join(ROOT, "data", "rawdata", file)
    target = path.join(ROOT, "data" ,"working", file)
    print(f"Copying file {file} from {source} to {target}")
    with open(source, 'rb') as f:
        data = f.read()
    with open(target, 'wb') as f:
        f.write(data)

def table_to_file(file, database = "test.db", table = "test", **_):
    sql = f"select * from {table}"
    with Database(database) as db:
        data = pd.read_sql_query(sql, db.connection)
        filepath = path.join(ROOT, 'data', 'output', file)
        print(f"Unloading table {table} from database {database} into file {filepath}")
        data.to_csv(filepath)
        