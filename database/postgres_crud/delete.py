from ast import Delete
from db_connect import db_connect

def get_connection():
    connection = db_connect()
    # once connected to the database, we can perform create , ... and more operations
    # user is the reserved word so can't create user table but if insist on doing so ? https://stackoverflow.com/a/22256451/9898251
    if(not connection) :
       print("No connection to the database found")
       exit()
    cursor = connection.cursor()  
    return connection, cursor 

def delete_data_from_users_table(name_to_be_deleted_like):
    connection,cursor  = get_connection() 
    try:
        # delete_query = 'DELETE FROM users where name=%s'
        # cursor.execute(delete_query, (name_to_be_deleted_like,)) # expects more than one value in tuple

        delete_query = 'DELETE FROM users where name ILIKE %s'
        cursor.execute(delete_query, ('%' + name_to_be_deleted_like + '%',)) # expects more than one value in tuple 
        print("Data deleted successfully")

    except(Exception, ConnectionError) as error:
        print("Error occurred : ", error)

    finally:
        connection.commit()
        connection.close()

delete_data_from_users_table('John Doe')            