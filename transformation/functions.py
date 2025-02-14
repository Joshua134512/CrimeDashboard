from connectors.SQL import Database
from os import path,curdir

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