def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

x = input("Enter number :")
fac = factorial(x)
print(fac)