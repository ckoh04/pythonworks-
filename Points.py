#distance= sqrt((x2-x1)^2 + (y2-y1)^2
import math

x1= (eval(input("Enter x1 value:")))
x2= (eval(input("Enter x2 value:")))
y1= (eval(input("Enter y1 value:")))
y2= (eval(input("Enter y2 value:")))

distance= math.sqrt(math.pow(x2-x1,2)) + math.sqrt(math.pow(y2-y1,2))
print ("The distance is:", distance)

