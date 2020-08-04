"A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type."
""" Accessing Dictionary : dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4

If the key is not there in the dictionaru it raises an error to avoid that we can use 
GET  method.GET moethod returns none if the value is not there.

Adding Items to a Dictionary:
ex: dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
    dct['key5'] = 'value5' 
    
Modifying Items in a Dictionary:
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'

Checking Keys in a Dictionary:
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

Removing Key and Value Pairs from a Dictionary
pop(key): removes the item with the specified key name:
popitem(): removes the last item
del: removes an item with specified key name

Changing Dictionary to a List of Items:
The items() method changes dictionary to a list of tuples :

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

dict.keys() : It will return keys in the dictionary
dict.values() : It will return the values """
dog = {}

dog = {"name":"Goofy","color":"Brown",}
