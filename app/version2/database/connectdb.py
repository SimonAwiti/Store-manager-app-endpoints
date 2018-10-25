import os
import psycopg2
"""import the list of tables"""
from .create_table import queries, drops

def dbconnection():
    """making a connection to the db"""
    url = os.getenv('DATABASE_URL')
    return psycopg2.connect(url)


def initializedb():
    try:
        """starting the database"""
        connection = dbconnection()
        connection.autocommit = True

        """activate cursor"""
        cursor = connection.cursor()
        for query in queries:
            cursor.execute(query)
        for drop in drops:
            cursor.execute(drop)
        connection.commit

    except (Exception, psycopg2.DatabaseError) as error:
        print("DB Error")
        print(error)

