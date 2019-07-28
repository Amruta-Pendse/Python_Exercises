#Program to find largest number

p=[]
def Larg_Num_Usr_Input(p):
    i=0
    while i< 3:
        n1=int(input("Enter number:"))
        p.insert(i,n1)
        i+=1

    
    if (p[0]>p[1] and p[0]>p[2]):
        print (p[0])  
    elif (p[1]>p[0] and p[1]>p[2]):
        print(p[1])      
    else:
        print(p[2])    

Larg_Num_Usr_Input(p)