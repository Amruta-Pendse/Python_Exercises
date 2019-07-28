#program to find sum of numbers

def number_sum(p):
    sum_all=0
    i=0
    for i in p:
        sum_all=sum_all+i

    return sum_all

x=[3,4,5,6,7]
num_sum=number_sum(x)
print(num_sum)


