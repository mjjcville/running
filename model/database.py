import sqlite3
from typing import Optional

class Database:
    connection: sqlite3.Connection
    cursor: sqlite3.Cursor
    
    def __init__(self, database_name:str) -> None:
        try:
            self.connection = sqlite3.connect(database_name)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as db_error:
            raise db_error
        
    def commit_changes(self) -> None:
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()
        
    def execute(self, sql_statement:str) -> Optional[sqlite3.Cursor]:
        try:
            result = self.cursor.execute(sql_statement)
            return result
        except sqlite3.Error as db_error:
            raise db_error
        
    def executemany(self, sql_statement:str, values:list[tuple]) -> Optional[sqlite3.Cursor]:
        try:
            result = self.cursor.executemany(sql_statement, values)
            return result
        except sqlite3.Error as db_error:
            raise db_error
        