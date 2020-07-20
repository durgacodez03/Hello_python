# strings only
first_name = "Python"
last_name = "language"
formatted_string = "The new technology is %s %s" % (first_name, last_name)
print(formatted_string)

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
print("The area of a circle with radius %d is %.2f" % (radius, area))

python_libraries = ['Django', 'Flask', 'Numpy', 'Pandas']
formated_string = 'The following are python libraries: %s ' % python_libraries
# "The following are python libraries:['Django', 'Flask', 'Numpy', 'Pandas']"
print(formated_string)

# str.format

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(
    first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
# limits it to two digits after decimal
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

#f-Strings(Python 3.6+)
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
print(f'my name is {first_name}')

# unpacking
language = 'Python'
print(list(language))
a, b, c, d, e, f = "python"  # unpacking the characters in to varaibles
print(a)
print(b)
print(c)
print(d)

# Acessing the characters (To fetch the character)
print(language[0], "accessing the characters")
print(language[:], "accessing the characters")
print(language[-1], "accessing the characters")
print(language[::-1], "accessing the characters")
print(language[-2], "accessing the characters")

# slicing (we can slice the strings into substrings)
print(language[0:3], "slicing the string")
print(language[-3:], "slicing the string")

# Skipping Characters While Slicing
word = "python"
print(word[1:5:2])  # [start:stop:step]
