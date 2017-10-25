import math
#a+b>C
#b+c>a
#a+c>b
a= eval(input("Enter a number:"))
b= eval(input("Enter a number:"))
c= eval(input("Enter a number:"))

s= (a+b+c)/2
if a+b>c:
    area= math.sqrt(s*(s-a)*(s-b)*(s-c))
    print ("The area is:", area)

else:
    print("Not a triangle! Check your values of sides!")
