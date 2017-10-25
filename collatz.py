"""
This program will generate Collatz sequence
f(n)= n/2 if n=0 (mod2)
      3n+1 if n=1 (mod2)
"""
#while "true"=="true":
print ("Enter any positive integer: ")
n =int(input())
count=0
while n!=1:
    if n%2 == 1 or n==0:
        n= int(3*n+1)
    else:
        n= int(n/2)
    print (n)
    count = count +1
print ("The repeating number is ", count)