#Program to covert Temperature from/to Celsius to Farenheit

n1=input("Enter 'C' to enter Temperature in Celsius and 'F' for Farenheit:")

if(n1=='C' or n1=='c'):
    ctemp= float(input("Enter Temperature in Celsius:"))
    ftemp=(ctemp*1.8) +32
    print("Temperature in Farenheit is:", ftemp)

elif (n1=='F' or n1=='f'):
    ftemp=float(input("Enter Temperature in Farenheit:"))
    ctemp=(ftemp-32)/1.8
    print("Temperature in Celsius is:",ctemp)
else:
    print("Not a valid value")        