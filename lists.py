#  List is a collection of multiple items. Like can include marks of 2000 students
#  In python we can declare list inside of the square brackets 
#  Syntax : variable_name = [value1, value2, ....., valuen]
#  Type of list gives <class 'list'>
#  List can contain mixed data types, [int, float, string, .. ]
#  List can be created using list() constructor as well. 
#  Lists are mutable , they can be changed, can be checked using id(list), before and after gives the same address.
#  Lists can be compared with >, < == operators
#  Items can be added at end, insert at specified position, removed, counted etc.

marks = [] # empty lists
marks_in_subjects = [90, 99, 66, 77, 88]
marks = marks_in_subjects # assign one list to another list.
print(marks)
print(type(marks_in_subjects), marks_in_subjects)

items = list() # empty list
fruits = list(['mango', 'banana', 'apple', 'orange', 'pineapple']) # Pass list inside of the constructor.
print(fruits[0], fruits[len(fruits)-1], fruits)

#  list inside of the list
list5 = [
    [33, 55, 77],  # first element
    [99, 31, 64]   # second element
 ]

print(list5[0][0])

range_list = list(range(5)) # list of numbers from 0 to 5[excluding]
print(range_list)

print(fruits[-1]) # print the last fruits

# Looping through the list
for fruit in fruits:
    print(fruit)

print(fruits[1:3]) # 

combined_list = fruits + ['litchi', 'fruit N']

languages = ['Python', 'Java']
print("\nList of language " + str(languages))
languages.append('Groovy') # adds to the last
languages.insert(0, 'Kotlin')
print(languages)
print(languages.index('Kotlin')) # gives the index of the Kotlin
languages.remove('Kotlin')
print(languages.count('Java'))
print(languages.sort()) # sorting in ascending order, 
print(languages.reverse())
languages.pop()
print(languages)





