your_age = input("Enter Your age:")

if int(your_age)<=18:
    print("You are old enough to drive")
else:
    print("Happy driving")

my_age = 35
if int(your_age) == int(my_age):
    print("we are of same age")
elif int(your_age) > int(my_age):
    var = my_age-your_age
    print("you are %d bigger than my age"%(var))
elif int(your_age) < int(my_age):
    var = (int(your_age) - int(my_age))
    print("you are %d smaller than my age"%(abs(var)))
else:
    print("Bye")

