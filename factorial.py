def fact(n):
    
    if n == 0:
        print("0! is 1")
    elif n == 1:
        print("1! is 0")
    else:
       i = 0
       fact = 1
       while i<n:
            fact = fact*(n-i)
            i  += 1
       
       return fact

print(fact(2))