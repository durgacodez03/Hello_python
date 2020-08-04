dog = {"name":"Goofy","age":12,"color":"White","Breed":"Snow"}

student_dict = {"first_name":"python","last_name":"coding","gender":"Lnaguage","country":"India"}

print(len(student_dict))

var = []
for x in student_dict.values():
    var.append(x)

print(var)
print(type(var))

college = {"name":["oxford","kerala","dkjdkj"],"place":"India"}
print(college["name"])

college["name"] = ["dkasdkja","jlaldlkl"]

print(college)

print(college.items())

print(college.keys())

print(college.values())      

del college['place']

print(college)

del student_dict