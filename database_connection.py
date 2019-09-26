import mysql.connector

#Context Manager class
#Holds the database connection information
class DatabaseConnection:
    def __init__(self):
        self.db_connection = None


    def __enter__(self) -> mysql.connector.MySQLConnection:
        self.db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root12345",
        database="milestone_project2"
    )

        return self.db_connection


    def __exit__(self, exc_type, exc_val, exc_tb):
        
        if exc_type or exc_val or exc_tb:
            self.db_connection.close()
        else:
            self.db_connection.commit()
            self.db_connection.close()
    