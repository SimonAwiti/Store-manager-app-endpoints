import os
import psycopg2
"""import the list of tables"""
from .create_table import queries

def db_connection():
    """making a connection to the db"""
    url = os.getenv('DATABASE_URL')
    return psycopg2.connect(url)

def initialize_db():
    try:
        """starting the database"""
        connect = db_connection()
        connect.autocommit = True
        print connect

        """activate cursor"""
        cursor = connect.cursor()
        for query in queries:
            cursor.execute(query)
            connect.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print error
