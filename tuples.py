"Tuples is an ordered and immutable data type"
empty_tuple = ()

print(empty_tuple)

# We can change tuples to lists and lists to tuples.
#  Tuple is immutable if we want to modify a tuple we should change it to a list.

bro_tuple = ("cat", "mat", "bat", "rat")
sis_tuple = ("apple", "banana", "mango", "citrus", "rat")

family = bro_tuple+sis_tuple

print(family)

print(len(family))

new_family = list(family)
new_family.extend(["Donkey", "Monkey"])
print(tuple(new_family))

family, *sibilings = new_family
print(family)
