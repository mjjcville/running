import sqlite3 
from model import database

#Define Table create query strings
create_table_project_sql:str = '''CREATE TABLE IF NOT EXISTS projects (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
description VARCHAR, 
updated_at VARCHAR,
created_at VARCHAR
) '''

create_table_project_membership_sql:str = '''CREATE TABLE IF NOT EXISTS project_memberships (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
project_id INTEGER NOT NULL, 
email VARCHAR, 
updated_at VARCHAR,
created_at VARCHAR,
FOREIGN KEY (project_id) REFERENCES project(id)
CONSTRAINT project_membership_email_project_unique UNIQUE (project_id, email)) '''
    
create_table_project_membership_api_key_sql:str = '''CREATE TABLE IF NOT EXISTS project_membership_api_keys (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
project_membership_id INTEGER NOT NULL,
secret_key VARCHAR, 
updated_at VARCHAR,
created_at VARCHAR,
FOREIGN KEY (project_membership_id) REFERENCES project_membership(id),
CONSTRAINT project_membership_api_secret_unique UNIQUE (secret_key)) '''

create_table_device_sql:str = '''CREATE TABLE IF NOT EXISTS devices (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
project_id INTEGER NOT NULL, 
description VARCHAR,
operating_system VARCHAR,
updated_at VARCHAR,
created_at VARCHAR,
FOREIGN KEY (project_id) REFERENCES project(id)) '''

create_table_device_api_key:str = '''CREATE TABLE IF NOT EXISTS device_api_keys (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
device_id INTEGER NOT NULL,
secret_key VARCHAR,
updated_at VARCHAR,
created_at VARCHAR,
FOREIGN KEY (device_id) REFERENCES device(id),
CONSTRAINT device_api_secret_unique UNIQUE (device_id, secret_key)) '''

create_table_event:str = '''CREATE TABLE IF NOT EXISTS events (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
device_id INTEGER NOT NULL,
event_type_id INTEGER NOT NULL,
description VARCHAR(100) NOT NULL,
status VARCHAR(15),
reported_updated_at VARCHAR NOT NULL,
updated_at VARCHAR,
created_at VARCHAR,
FOREIGN KEY (device_id) REFERENCES device(id),
FOREIGN KEY (event_type_id) REFERENCES event_type(id)) '''

create_table_event_type:str = '''CREATE TABLE IF NOT EXISTS event_types (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
short_name VARCHAR(15) NOT NULL,
description VARCHAR, 
updated_at VARCHAR,
created_at VARCHAR,
CONSTRAINT event_type_short_name_unique UNIQUE (short_name)) '''


#Connect to the new database
try:
    device_observer_database = database.Database("device_observer_app.db")

    #Run the create statements
    device_observer_database.execute(create_table_project_sql)
    device_observer_database.execute(create_table_project_membership_sql)
    device_observer_database.execute(create_table_project_membership_api_key_sql)
    device_observer_database.execute(create_table_device_sql)
    device_observer_database.execute(create_table_device_api_key)
    device_observer_database.execute(create_table_event)
    device_observer_database.execute(create_table_event_type)

    print (f"Database created successfully")
except sqlite3.Error as db_error:
    print (f"Database Error: {db_error.sqlite_errorcode}, {db_error.sqlite_errorname}")