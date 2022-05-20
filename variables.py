# Variables are used to store values
# Python language is interpreted, meaning it executes line one by one unlike compiled language
# Python is Strongly Typed , i.e doen't convert type automatically "this is number" + 12 would produce error , have to convert 12 to string as str(12)
# In python variables are created as : variable_name = expression eg age = 22
# Type of variable can be checked using type(variable) 
# In python variables can be assigned a different value like str = "6" and later str = 6 is fine
# Python doens't have special type for constant variables but we use UPPERCASE letter to denote constant.
# In python simultaneous assignment is possible as :  var1, var2, var3, ...  varN = exp1, exp2, exp3, ... expN
# declare variables and assign values to them
message = 'Hello ' #String Variable
name = 'John Doe'
age , AGE_MESSAGE = 20, " years old" # simultaneous assignment


# Prints to the console 
# print(type(message)) # gives <class 'str'>
# print(message + name + " you're " + age + " years old") # gives error as str and int can't be converted. 
# str(value) converts value to type string , print(type(str(4))) gives <class 'str'>
print(message + name + " you're " + str(age) + AGE_MESSAGE) 
print(message, name, " you're", str(age), AGE_MESSAGE) # printing multiple values 
# print(help(input)) # gives help about input in python