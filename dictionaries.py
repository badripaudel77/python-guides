# Dictionaries are key value pair just like in normal English-Nepali dictionary
# In python dictionary can be created using key-value pair, inside of the curly bracket. {key: value, ....}
# Type of dictionary gives : <class 'dict'>
# Value in dictionary can be accessed using its key as dict.get('key') or dict['key']
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# Dictionaries cannot have two items with the same key: Duplicate values will overwrite existing values
# The values in dictionary items can be of any data type


vehicle = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "is_nice" : True
}

print(type(vehicle), vehicle)
print(len(vehicle))

print("Brand of the vehicle is : ", vehicle.get('brand'), 'And model year is : ', vehicle['year'])

for _key in vehicle:
    print(_key, ' => ', vehicle.get(_key))
print("--------")    

for key, value in vehicle.items():
    print(key, value)