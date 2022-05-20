# Formatting in different formats 
#  Python has function to format to represent in various formats, format()

p = 18819.99    # principal
r = 0.05        # rate of interest
t = 2           # years

# format has syntax ::  format(value, format-specifier)

#The value is the data we want to format.
# The format-specifier is a string which determines how to format the value passed to the format() function.
# On success format() returns a formatted string.

interest = p * t * r
print("Simple interest at the end of " + str(t) + " years is $" +  str(interest))

interest = format(interest, ".2f") # after ., 2 floating digits
print("Simple interest at the end of " + str(t) + " years is [formatted] $" +  str(interest))

# https://overiq.com/python-101/numbers-in-python/
#  len of value to be formatted is : 6, but precision after . is just 2 [.2f], now len becomes 5 but format 
# specifier len is 9 so 9-5 = 4 spaces will be printed first and then formatted value
print(format(34.712, "9.2f")) # outputs :     34.71

print(format(00000.212354, ".3E"))

print(format(98813343817.7129, ",.2f"))

print(format(0.71981, "%"))

print(format(4, "b")) # binary representation of 4, x for hexa-decimal, 0 for octal
