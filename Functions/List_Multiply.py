#Program to multiply all the numbers in the list
l=[]
def Num_Multi(l):
    i=0
    multi=1
    for i in l:
        multi*=i
    return multi

p=[2,3,4,5,6]
print(Num_Multi(p))