import sqlite3 
from model import database

#Define Table create query strings
create_table_sleep_sql:str = '''CREATE TABLE IF NOT EXISTS sleep_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    sleep_date TIMESTAMP,
    average_hrv INTEGER,
    updated_at TIMESTAMP,
    created_at TIMESTAMP
) '''

#Connect to the new database
try:
    running_journal_db = database.Database("running_journal_app.db")

    #Run the create statements
    running_journal_db.execute(create_table_sleep_sql)

    print (f"Database created successfully")
except sqlite3.Error as db_error:
    print (f"Database Error: {db_error.sqlite_errorcode}, {db_error.sqlite_errorname}")