import math
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
D = (b*b)+(-1*(4*a*c))
if D < 0:
    print("Нет корней")
elif D > 0:
    sqrtD = math.sqrt(D)
    x1 = (sqrtD-b) / (2*a)
    x2 = (-b-sqrtD) / (2*a)
    print("x1={0};x2={1}".format(x1,x2))
elif D == 0:
    x = -b/4*a*c
    print ("x=",x,sep='')
else:
    print("Произошла ошибка")
