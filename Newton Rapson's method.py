#Newton Rapson Method
#Noa Asulin , Michal Tenenboim, Renana Zinner
import sympy as sp
from sympy.utilities.lambdify import lambdify
from sympy import *
import math
x = sp.symbols('x')
from datetime import datetime

#f = cos(x**2+5*x+6)/2*math.e**(-1*x)
#f_prime = f.diff(x)
#print(f)
#print(f_prime)

#f2 = (2*x*math.e**(-1*x)+ln(2*x**2))*(2*x**2-3*x-5)
#f2_prime = f2.diff(x)
#print(f2)
#print(f2_prime)

def Newton_Rapson(func, func2, num, count):
    epsilon = 0.0001
    if func(num) == 0:
        return num, count
    else:
        valFunc = func(num)
        valDiff = func2(num)
        result = num - (valFunc / valDiff)
        if abs(result - num) < epsilon:
            return result, count
        else:
            count = count + 1
            print("Interim results-",result)
            return Newton_Rapson(func, func2, result, count)

def Parts (a, b):
    count = (b-a)/0.1
    return count

def check (a, b, func):
    if func(a) * func(b) < 0:
        return 0
    else:
        return 1

#The main function
def main():
    a = -1.5
    b = 2
    my_f = cos(x**2+5*x+6)/2*math.e**(-1*x)
    my_f1 = sp.diff(my_f)
    print(my_f)
    print(my_f1)
    my_f = lambdify(x, my_f)
    my_f1 = lambdify(x, my_f1)


    amount = int(Parts(a, b))
    for i in range(amount):
        new = a + 0.1
        if check(a, new, my_f) == 0:
            count = 0
            start_x = (a + new) / 2
            result, count1 = Newton_Rapson(my_f, my_f1, start_x, count)
            print("")
            print("btween", a, " to ", new)
            print("The root of the equation in the segment is:", format(result)+"00000"+format(d)+format(hour)+format(minute))
            print("Number of iterations:", count1)
            print("")
            a = new
        else:
            a = new
            print("there is no roots")

date = datetime.now()
d = date.day
hour = date.hour
minute = date.minute

main()