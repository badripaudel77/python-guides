"""
To create a table, we can execute .execute(...) method from the cursor gotten in connection returned by the db_connect() method 

commit() function saves the changes to the database.
"""

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

def create_table():
  connection,cursor  = get_connection() 
  # Create the table
  create_table_users_query = 'CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, name VARCHAR(10),age INT)'
  try:
      cursor.execute(create_table_users_query)
      print("Query executed [table created]")
      # connection.rollback() # undo the undesirable changes 
  except(Exception) as error:
    print("Exception occurred : ", error)  

  # commit the changes
  connection.commit()
  # close the connection
  connection.close()

# Insert into table
def insert_into_users(id, name= 'John Doe', age = 0):
    connection,cursor  = get_connection() 
    insert_into_users_query = 'INSERT INTO users values(%s, %s, %s)'
    try:
        #print(cursor.execute(insert_into_users_query, (id, name, age))) # returns None
        cursor.execute(insert_into_users_query, (id, name, age))
        print("Data inserted into users table")

    except(ConnectionError) as connection_error:
        print("Something went wrong while inserting into database : ", connection_error)
    # commits the changes made to the database
    connection.commit()
    # Close the connection
    connection.close()

create_table() 
#insert_into_users(1, 'Badri', 25) # id can be made auto-incremental as well
insert_into_users(2) # default params will be used




