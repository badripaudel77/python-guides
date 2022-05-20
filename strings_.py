#  In python strings are represented using  single ('') or double quotation ("") marks

# In python to count no of characters [calculating length of string ] we use len(str) function

# Python strings can be compared using relational operators, > <, == but 
# Strings in Python are compared using the ASCII value of their corresponding characters.

# String objects are immutable. It means that we can't change the content of a string object after it is created.

programming_langugage = "Python"
programmer = 'Badri Paudel'


print(type(programmer), type(programming_langugage))

print("Length of "+ programming_langugage + " is " + str(len(programming_langugage)))

whos = 'John\'s' #
print(whos)

# string * n [can be used to repeat string ] n = whole number 

print("w" * 3) # repeats w three times.

fruit = 'Mango'
print("First letter of the fruit " + fruit + " is " + fruit[0])
print("Last letter of the fruit " + fruit + " is " + fruit[len(fruit) -1])

# slicing
print("hello"[0:3]) # 0 to 3[exclude]
print("hello"[3:]) # 3 to end
print("hello"[:3]) # to 3
print("hello python"[2:-1]) # 0 to len , 0, 1, : -ve : -1, -2 , .. - len

# 
print("he" == "he", "she" < "see", 'he' != 'hey')

print("badri".upper())
print("lowercase".isupper())

# strip() is used to remove leading & trailing spaces
college = "   NCIT     "
print("College = " + college.strip().capitalize())

# various other methods are : isdigit(), find(), startswith(sub), endswith(sub) etc. 

lang = 'groovy'
print(id(lang)) # id gives the address of the object
lang = lang + '-'
print(id(lang)) # id gives the address of the object but completely different address is created as strings are immutable

lang[0] = 'G' # gives error as string is immutable


