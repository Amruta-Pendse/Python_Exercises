# Accept Radius of Circle and compute Area of Circle

while True:
    n1=float(input("Enter the radius of circle:"))

    if (n1==0):
        print("Enter a non-zero value.")
        continue
    elif (n1<0):
            print("Enter a value greater than zero.")
            continue
    elif n1>0:
        print("Area of circle is ", 3.14*n1*n1)
        break
            
print("Area of circle calculated.")        
