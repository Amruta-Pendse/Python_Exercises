# Adding Substring at the end of String'

ch='a'
counter=0
str= input("Enter any string Value:")

for ch in str:
    counter+=1

if counter<3:
    print("String value is:", str)
else:
    if (str[counter-3:counter])=='ing':
        str=str+'ly'
        print("String value is", str)
    else:
        str=str+'ing'
        print("String value is", str)