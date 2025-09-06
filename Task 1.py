# Factorical

# 0! = 1
# 1! = 1*0! =1 *1 = 1
# 2! = 2*1! = 2
# 3! = 3*2! = 6
# 4! = 4*3! = 24

n= int(input("Enter a number for finding the factorial: "))
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print("Factorial of ",n,"is :", factorial(n))