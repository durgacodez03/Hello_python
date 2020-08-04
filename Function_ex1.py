"Declare a function add_two_numbers. It takes two parameters and it returns a sum."

def add(x,y):
    result = x+y
    return result

print(add(4,5))

"Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle."
def area_circle(r):
    pi = 3.14
    area = pi * r * r
    return area

print (area_circle(5))

"Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types./n"
"If not do give a reasonable feedback."

def add_all(*nums):
    j=0

    for i in nums:
        if isinstance(i, int):
            j = i+j
            print("The sum of all numbers are %d"%(j))
        else:
            print("They are not integer data type")

add_all(1,2,3,4,'a')

"Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celcius_to-fahrenheit."

def temp_conversion(centigrade):
    "°F = (°C x 9/5) + 32"
    farenheit = (centigrade * 9/5) + 32
    print(farenheit)

temp_conversion(98)


"Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer."

def check_season(Month):
    if Month == "Jan":
        return "Winter"
    elif Month == "Feb" and "March":
        return "Autumn"
    elif Month == "April" and "May":
        return "Summer"

print(check_season("Jan"))

"Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list."
def print_list(var):
    for x in var:
        print(x)

var_list = [1,2,3,4,5]
print_list(var_list)

"Reverse_list"

def reverse_list(var):
    length = len(var)
    s = length
    new = [None] * length

    for i in var:
        s = s-1
        new[s] = i
    print(new)

reverse_list(var_list)

def capitalize_list_items(var):
    for i in var:
        if i.isupper():
            print (i)
            print("These are capital letters")
        else:
            print("Check here",i)
            i.capitalize()
            print(i)

letters = ["a","B","C","d","e"]
capitalize_list_items(letters)
    
def add_item(var):
    var.append(6)
    print(var)

new = [1,2,3,4,5]
add_item(new)

def factorial(n):
    
    if n is 0:
        print("0! factorial is 1")
    elif n is 1:
        print("1! factorial is 1")
    else:
        i = 0
        fact = 1
        while i<n:
            fact = fact*(n-i)
            i  += 1
        
        print("The factorial of the number %d is %d"%(n,fact))

factorial(6)


"Call your function is_empty, it takes a parameter and it checks if it is empty or not"

def is_empty(var):
    if len(var)!=0:
        print("This is not empty")
    else:
        print("This is empty")
    
new_list = [ ]
is_empty(new_list)

"Write a function which check if provided variable is a valid python variable"
def check_valid(var):
    if var.isidentifier():
        print("valid")
    else:
        print("Not valid")

x = '2'
check_valid(x)

"Prime Numbers"
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for i in range(2,n+1):
            if (n%i == 0):
                return False
            return True

print(test_prime(8))
