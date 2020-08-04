# Create an empty set :
empty_set = {}

"or"

set()

"""Sets are unordered and unindexed. They are immutable we cannot insert the element but
we can update the elements and there wont be any duplicate elements.
add() : It will add only one element
update() : It will update set of elements.
subset() : A is the subset of B means All the elements of Should be in B
superset() : A is the superset of B means all the elements of B should be in A
uniion : Combination of all the elements 
Intersection : Common elements 
Difference : A-B : Which elemnets are not there in B it will return A
Symmentric diffrenece : Opposite to difference 
disjoint : Elements which are not in common"""

fruits = {'banana','orange','appple'}
print(len(fruits))

print(set(fruits))

# Examples :
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add("Twitter")

print(it_companies)

it_companies.update(["ust","intel"])
print(it_companies)

new = A.union(B)
print(new)

common = A.intersection(B)
print(common)

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.union(B))
print(B.union(A))

del A



var = "I am a teacher and I love to inspire and teach people"
new = var.split(" ")
print(new)

print(new.count("I"))
