"""
There are several python modules that allow us to connect to and manipulate the database using PostgreSQL, one of them 
is  Psycopg2
To install Psycopg2, we can run the command 
```sudo pip3 install psycopg2``` 
once installed, we can import it and get various available methods.
"""

# This file will create connection to the PostgreSQL database server on my local machine and return it so that it can be used in other files

import psycopg2

def db_connect():
    connection = None
    try:
        connection = psycopg2.connect(
                            database ="python_guides", 
                            user = "postgres", 
                            password = "_BadriPostgres1@", 
                            host = "localhost", 
                            port = "5432")
        # print("connected to the DB : ", connection)                    

    except(Exception) as error:
        print("Something went wrong while connecting to PG DB server : ", error)

    finally:
        return connection   

# print(db_connect().cursor())            
