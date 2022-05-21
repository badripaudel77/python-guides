#  Tuples are unchangable collection of multiple items that maintains the order.
#  In python tuples are created using () parenthesis.
#  Since tuples are 'indexed', it can allow duplicate items
#  Type of tuple type(tuple) gives : <class 'tuple'>
#  Also can be created using tuple constructor as tuple(tuple_value)

fruits = ('Apple', 'Mango', 'Banana')

print(type(fruits), fruits)

index_of_apple = fruits.index('Apple')
print("Index of Apple in tuple is : ", index_of_apple)
print("Length of tuple is ", len(fruits))

items = tuple(('item1', 'item2', 'item3'))
print(type(items), items)