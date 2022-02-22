# question 13 part 2:
from math import e, sqrt, log
from numpy import log as ln
# from math import sqrt
from math import cos
import sympy as sp
from datetime import datetime

# from math import erf
# from sympy.utilities.lambdify import lambdify


def g(f):
    return (e**-f*(f*(e**f*(6*(4*f**2-9*f-30)*(log(sqrt(2)*abs(f)))-8*f**2+27*f+180)-36*(f+1)*(2*f+1))-36))/18


x = sp.symbols('x')


def f(a):
    return (2*a*e**-a+log(2*a**2))*(2*a**2-3*a-5)


def verify():
    """Check that 2nd-degree polynomials are integrated exactly."""
    a = 0.5
    b = 1
    n = 2   # test integrand
    exact = g(b) - g(a)  # integral of g
    approx = simpson(f, a, b, n)
    if abs(exact - approx) > 1E-14:
        print("Error: Simpson's rule should integrate g exactly")
    return approx


def simpson(f, a, b, n=500):
    """
    Return the approximation of the integral of f
    from a to b using Simpson's rule with n intervals.
    """
    if a > b:
        print('Error: a=%g > b=%g' % (a, b))
        return None

    # Check that n is even
    if n % 2 != 0:
        print('Error: n=%d is not an even integer!' % n)
        n = n+1  # make n even

    h = (b - a)/float(n)
    sum1 = 0
    for i in range(1, n//2 + 1):
        sum1 += f(a + (2*i-1)*h)

    sum2 = 0
    for i in range(1, n//2):
        sum2 += f(a + 2*i*h)

    integral = (b-a)/(3*n)*(f(a) + f(b) + 4*sum1 + 2*sum2)
    print("f(a) is:", f(a))
    print("f(b) is:", f(b))
    return integral


a = round(verify(), 6)
date = datetime.now()
d = date.day
hour = date.hour
minute = date.minute
print("the answer is:",format(a)+("00000")+str(d)+str(hour)+str(minute))