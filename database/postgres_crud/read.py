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

def fetch_from_users_table():
    connection,cursor  = get_connection() 

    try:
        fetch_query = "SELECT * FROM users" #SELECT * FROM users LIMIT 1
        cursor.execute(fetch_query)
        # store the data 
        data = cursor.fetchall()
        print_data(data)
    except(ConnectionError, Exception) as error:
        print("Something went wrong while fetching records from the database : ", error) 
    finally:
        cursor.close()
        connection.close()      

# Receives the data and prints it
def print_data(data):
    print("All the users in the database : ")
    for one_row in data:
        #print(type(one_row)) # one_row is entire row as  (1, 'Badri', 25) [Tuple]
        print(one_row[0] , one_row[1], one_row[2])

# call fetch_from_users_table() method
fetch_from_users_table()