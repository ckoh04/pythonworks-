import math
#height= (velocity*t)-(1/2*g*t^2)

#m= eval(input("Enter meters:"))
t= eval(input("Enter time:"))
velocity= eval(input("Enter velocity:"))


g= 9.8

height = (velocity*t)-((g*math.pow(t,2))/2)
print ("The height is:",height)
