# Functions in python are defined as:
#  def function_name(args......): body
# In function return keyword can be used to return values from that function.
# In python we can return multiple values from a function just specify each value separated by comma (,) after the return keyword.

import datetime

today = str(datetime.datetime.now()) # global variable, accessible everywhere
def greet_user(message) :
    hello = "Hello" # local, only accessible inside this function
    print(hello + message + " on " + today)

greet_user("User")
greet_user("Badri Paudel")

def add_numbers(a, b):
    result = a + b
    return result, a,b # python can return multiple values

sum, n1, n2 = add_numbers(23, 7) 
print("sum of two numbers " + str(n1) + " and " + str(n2) + " is " + str(sum))     
