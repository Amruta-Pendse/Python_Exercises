#Program to find factorial of a given number


def facto(n):
    i=1
    fact=1
    while i<=n:
        fact*=i
        i+=1
    return fact
facto(7)
print(facto(7))