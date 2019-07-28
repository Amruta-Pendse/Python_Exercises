# Program to reverse a string

def String_Reverse():
    str=input("Enter a string:")
    i=0
    j=0
    l=[]
    for i in str:
        l.insert(j,i)
        j+=1

    l.reverse()

    print("Reverse of",str, "is:",end="")
    for j in l:
        print(j,end="")
    print("\n")    
              
String_Reverse()        