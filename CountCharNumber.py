# Program to count the number of characters and numbers in a string

str=input("Enter a string with numbers:")
chcnt=0
nucnt=0
l1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digit=['1','2','3','4','5','6','7','8','9','0']

for ch in str:
    if (ch in l1 or ch in l2):
        chcnt+=1
        continue   
    else:
        if ch in digit:
            nucnt+=1
        else:
            continue     

        

print("Number of Characters in String are:",chcnt)
print("Number of Digits in String are:",nucnt)
