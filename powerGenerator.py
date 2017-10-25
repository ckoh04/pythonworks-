"""
This program will print the powers(exponents) of a number (base).

"""
base= eval(input("Enter the base number:"))
exponent = eval(input("Enter the maximum exponent"))
count = 0

if (exponent == 0):
    print ("1")
else:
    print (base)
result = base
while count < exponent - 1:
    result = result * base
    print (result)
    count= count+1
