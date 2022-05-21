# Set also can contain multiple not duplicating values.
# In python set can be created using {} curly bracket pair
# Type of set gives : <class 'set'>
# Just like other collections, set constructor also can be used to create set
# We cannot access items in a set by referring to an index or a key.
# But we can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
# Add to python set can be done with set.add('value')

# Cannot get set's value using index but can convert that to list and get based on index of as list items can be accessed using index

fruits = {"apple", "banana", "mango"} 

print(type(fruits), fruits)

lang = {'Nepali', 'Spanish', 'English'}
languages = set(lang)
languages.add('Portuguese')
print(type(languages), languages)
languages.pop()
print(languages)

for language in languages:
    print(language)

languages_list = list(languages)
print('Index access : ' , languages_list[len(languages)-1])