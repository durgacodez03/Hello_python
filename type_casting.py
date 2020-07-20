# int to float

num_int = 10
print('num_int', num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int

gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int
num_str = '10'
print('num_int', int('10'))
print('num_float', float(int(num_str)))

# str to list
first = 'Asabeneh'
print(first)  # 'Asabeneh'
first_name_to_list = list(first)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
