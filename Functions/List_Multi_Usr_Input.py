#Program to multiply numbers taking input from User

l=[]
def List_Multi(l):
    num_in=int(input("Enter the number of numbers needed in list:"))
    i=0
    j=0
    multi=1
    while i<num_in:
        n1=int(input("Enter number:"))
        l.insert(i,n1)
        i+=1
    for j in l:
        multi*=j
    return multi

print(List_Multi(l))   


