#Program to check if a number is prime number



while True:
    InputNumber=int(input("Enter any number to check if it is prime or not:"))
    
    if InputNumber==1:
        print("Enter value greater than 1.")
        continue
    elif InputNumber==0:
        print("Not a valid number to check")
        break
    elif InputNumber==2:
        print(InputNumber, "Is a Prime number")
        break
    else:
        i=0
        for i in (2,InputNumber-1):
            counter=0
            if (InputNumber%i==0):
                counter=1
                break
        if counter==1:
            print(InputNumber, " Is not a Prime number")
            break
        else:
            print(InputNumber, " Is a Prime number") 
            break                      
          
    