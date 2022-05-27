# File handling in Python

# common operations 

# https://stackoverflow.com/questions/44901806/python-error-message-io-unsupportedoperation-not-readable

# 1. Open the file
# file = open('/Users/badripaudel/PythonCodes/python-guides/file_handling/file.txt', 'r') #absolute path : path from the root directory '/User/.... /file-handling'
file = open('file.txt', 'r') #relative path : path from the current directory 'file-handling'

#get the properties of the file
print('Name of the file is : ', file.name)
print('Mode of the file is : ', file.mode)

print('read all the content once : ', file.read())
# print('Single line Content of the file is : ', file.readline()) # reads single line

contents = file.readlines()
print('All the Content of the file is : ', contents) # reads all the  lines and return as list of string
file.close()

# 2. Write to the file
# open the file
file_name = open('hello_python.txt', 'r+') # r+ for both reading & writing
file_name.write('Python is nice but it\'s indentation sucks sometimes')
print(file_name.read())
file_name.close()