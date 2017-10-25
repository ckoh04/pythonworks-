#This program will compute fibonacci sequence from an entered number.
num= eval(input("Enter a number:"))
a,b= 0,1
for i in range (num):
    print (a,end= " ")
    f= a+b
    a= b
    b= f
print (" ")