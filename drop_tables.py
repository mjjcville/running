from model import database
import sqlite3

tables:list[str] = [
    'sleep_info',
    'weather_info',
    'running_info'
]

database_name:str = "running_journal_app.db"

try:
    for table in tables:
        drop_sql_statement: str = "DROP TABLE IF EXISTS " + table
        runnning_journal_database = database.Database(database_name)
        runnning_journal_database.execute(drop_sql_statement)
        runnning_journal_database.close()
        print (f"Database table {table} dropped successfully.")
except sqlite3.Error as db_error:
    print (f"Database Error: {sqlite3.Error.sqlite_errorcode}, {sqlite3.Error.sqlite_errorname}")