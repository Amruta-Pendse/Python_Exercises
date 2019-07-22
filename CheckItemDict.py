# Program to check key is available in Dictionary

d1={'red':'Rose','green':'Leaf','blue':'Sky','yellow':'SunFlower','white':'Milk','black':'Hair','pink':'Dream'}

key=input("Enter any color name to search:")

for i in d1:
    if key==i:
        print(d1[i])
        break      
else:
    print("Mentioned color not in dictionary")    
