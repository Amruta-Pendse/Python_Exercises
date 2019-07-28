# Sum of all numbers in a list

p=[]
def sum_of_nums(p):
    number_count=int(input("Input the number of numbers you want to input:"))
    i=0
    while i<number_count:
        n1=int(input("Enter number:"))
        p.insert(i,n1)
        i+=1
    print(p)

    sumall=0
    j=0
    for j in p:
        sumall+=j    
    print(sumall)


#sum_of_numbers=sum_of_nums(p)
sum_of_nums(p)