#Program to print square of numbers between 1 and 30

def num_sq():
    l=[]
    n=0
    i=1
    while (i<=30):
        n=i*i
        l.insert(i-1,n)
        i+=1

    print(l)

num_sq()    