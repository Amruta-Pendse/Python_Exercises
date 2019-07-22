# Find the largest number from list taking the values from user

l1=[]
i=0
count=int(input("enter the number of values you want to provide:"))
print("Enter any",count," values for list:")

while i<count:
    n1=int(input("Enter number:"))
    l1.insert(i,n1)
    i+=1

n=0
largest=l1[0]
for n in l1:
    if (n>largest):
        largest=n


print("Max number from list is:", largest)