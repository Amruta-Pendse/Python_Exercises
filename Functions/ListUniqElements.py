#Program to print unique elements from list

def uniq_elements():
    n=int(input("Enter number of elements you want to enter for list:"))
    i=1
    l=[]
    p=[]

    while (i<=n):
        n1=int(input("Enter {} number:".format(i)))
        l.insert(i,n1)
        i+=1
    print(l)
    
    i=0
    for i in l:
        j=i
        if (i in p):
            continue
        else:
            p.insert(j,i) 
               
    print(p)        

uniq_elements()    
