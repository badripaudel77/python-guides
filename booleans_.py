# used to represent if value is true or false
# type of boolean gives <class 'bool'>
# values  True or False 

# Truthy values: Values which are equivalent to bool value True is known as Truthy values. eg 1, 2, some values just like in groovy

# Falsy values: Values which are equivalent to bool value False is known as Falsy values. like 0, None, False, emptyp dictionary {}

# In python we can check if value is Truthy or Falsy using function called bool() 

is_final = True
print(type(is_final)) #<class 'bool'>

print(bool(0), bool("hello"), bool("0"), bool(99))

# Has same combination of Truthy & Falsy values as in other programming language or logic ckt
print(False and True, False and False, False or True, True and True, not True)