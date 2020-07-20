# variables
first_name = "Coding"
last_name = "python"
full_name = "Data science"
country = "India"
city = "Coorg"

print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)

# len of the variable

print(len(first_name))

# Compare first name and last name
if (len(first_name) == len(last_name)):  # For comparing 2 variables we use == operator
    print("Hello python")
else:
    print("Bye python")

# variable declaration
num_one = 5
num_two = 4

variable_total = num_one + num_two
print(variable_total)

variable_diff = num_two - num_one
print(variable_diff)

variable_product = num_one * num_two
print(variable_product)

variable_division = num_one/num_two
print(variable_division)

variable_remainder = num_one % num_two
print(variable_remainder)

variable_exponential = num_one**num_two
print(variable_exponential)

variable_floor_div = num_one//num_two
print(variable_floor_div)

# Calcualte radius of circle
circle = 30
pi = 3.14
area_of_circle = (pi)*(circle**circle)
print(area_of_circle)

# Calculate circumference of a circle
circumference = 2*pi*circle  # Formula : 2*pi*r
print(circumference)

# Take radius as user input and calculate the area
radius = int(input("Enter the radius"))
area_of_circle = pi*(radius**radius)
print("Based on the user input:", area_of_circle)
