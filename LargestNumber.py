# Find the largest number from list

l1=[]
i=0
print("Enter any 10 values for list:")

while i<10:
    n1=int(input("Enter number:"))
    l1.insert(i,n1)
    i+=1

print("Max number from list is:", max(l1))