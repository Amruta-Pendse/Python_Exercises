#Program to find if the string is a Palindrome

def String_Palindrome():
    str=input("Enter a string:")
    j=len(str)-1
    str1=""
    while j>=0:
        str1=str1+str[j]
        j-=1
    print (str1)

    if(str1==str):
        print("Entered string is a Palindrome")
    else:
        print("Entered string is not Palindrome")    

String_Palindrome()   