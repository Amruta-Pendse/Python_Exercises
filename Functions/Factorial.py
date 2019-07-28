#Program to find factorial of a given number


def facto():
    n1=int(input("Enter the number to find factorial:"))
    i=1
    fact=1
    while i<=n1:
        fact*=i
        i+=1
    return fact

print(facto())