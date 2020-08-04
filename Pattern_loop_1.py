'''def hash_print(n):
    for i in range(n+1):
        for j in range(0,i+1):
            print("*",end = " ")
        print("\n")

hash_print(7)'''
'''
def pattern_print(n):
    for i in range(n+1):
        for j in range(0,n+1):
            print("*",end=" ")
        print("\n")

pattern_print(8)'''

def pattern_multiply(n):

    for i in range(n+1):
        j = i * i
        print("%d * %d = %d"%(i,i,j))
    print("\n")

pattern_multiply(10)
