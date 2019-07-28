#Program to check and print even numbers from a list

def Even_Num_In_List():
    n1=[]
    n2=[]
    i=1
    j=0
    num_elements=int(input("Enter the number of elements required:"))
    while i<=num_elements:
        n=int(input("Enter {} number:" .format(i)))
        n1.insert(i,n)
        i+=1
    print("Entered List elements are:")
    print(n1)    

    for j in n1:
        p=j
        if j%2==0:
            n2.insert(p,j)
    print("Even numbered elements from the list are:")
    print(n2)    

Even_Num_In_List()