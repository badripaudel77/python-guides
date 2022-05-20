#  In python we have following main types as numbers 
# 1.Integer.
# 2.Floating Point or Real Numbers.
# 3.Complex Numbers.


# Integer type
age = 25
print(type(age))

# Float type [decimals]
potato_price_per_pound = 23.9
print(type(potato_price_per_pound))

# complex numbers
position = 4 + 5j
print(type(position))

number1 = 34
number2 = 34.80
result = number1 + number2
print("Addition gives : " + str(result))

alaska_temp = -20
print("absolute value of alaska temperature [" + str(alaska_temp) + " deg C] is " + str(abs(alaska_temp)))

print("2^5 = " + str(pow(2,5)))

PI = 3.14159265359
print("After rounding , the value of PI is " + str(round(PI, 2))) # round to 2 digits after decimals

print("min of 23 & 45 is " + str(min(23, 45)))

# exponentiation operator ** 
print("2 raise to the power of 5 is : " + str(2**5))

# / operator gives the float as a result 
print("20 divided by 10 is " + str(20/10))

# // operator gives the integer as a result 
print("20 divided by 10 is " + str(20//10))

# remainder operator gives the remainder of the division operation
print("20 divided by 7 gives remainder of  " + str(20 % 7))

x= 10
x += 100
incremented_x = x
print("x after incrementing by 100 is " + str(incremented_x))
