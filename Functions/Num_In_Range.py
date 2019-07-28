#Program to check if a given number is in range

def Num_in_Range():
    a=10
    b=100
    n1=int(input("Enter a number to check if in range:"))
    if n1>=a and n1<=b:
        print("{} is in given range of {} and {}" .format(n1,a,b))
    else:
        print("{} is not in given range  of {} and {}" .format(n1,a,b))

Num_in_Range()