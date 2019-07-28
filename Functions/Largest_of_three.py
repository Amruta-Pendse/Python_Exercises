# Program to find largest of 3 numbers

def Largest_of_three(a,b,c):
    if (a>b and a>c):
        return a
    elif b>a and b>c:
        return b
    else:
        return c

Largest_of_three(67,34,89)       
print(Largest_of_three(67,34,89))

Largest_of_three(7,3454,89)       
print(Largest_of_three(7,3454,89))

Largest_of_three(732,4,18)       
print(Largest_of_three(732,4,18))