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

def update_data_in_users_table(new_name):
    connection,cursor  = get_connection() 
    try:
        update_query = "UPDATE users set name = %s where name= %s"
        cursor.execute(update_query, (new_name, 'John Doe'))
        print("Data updated successfully")
    except(Exception, ConnectionError) as error:
        print("Error occurred : ", error)  

    finally:
        connection.commit()
        connection.close()

update_data_in_users_table('Smith Doe')              