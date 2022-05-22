# In python, exceptions can be handled using a try statement.
# The code that handles the exceptions is written in the except clause.
# sys.exc_info()[0] gives the error message just like e.getMessage() in java.
# We can catch specific error by passing type of error we want to handle in the constructor function of the except(....)

import sys

value = 10000
div_number = 0
result = 'NA'
status = False

try:
    result = value / div_number
    status = True   

# Catches specific error
except(ZeroDivisionError) :
    print('something went wrong, error message is : ' , sys.exc_info()[0])    

# if above except block doesn't catch, all will be catched by this except.
except(Exception):
    status = False
    print('something went wrong, error message is : ' , sys.exc_info()[0])  

finally:
    print('operation completed with status ', status , ' and result is : ', result)

# another demo
items = ['item1', 'item2'] 

try:
    print('Third items is ', items[2]) # gives error

# Catches specific error
except(ZeroDivisionError) :
    print('something went wrong, error message is : ' , sys.exc_info()[0])    

# if above except block doesn't catch, all will be catched by this except.
except(Exception):
    print('something went wrong, error message is : ' , sys.exc_info()[0])  
