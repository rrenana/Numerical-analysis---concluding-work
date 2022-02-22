# Defining Function
# question for ln
from math import e
from numpy import log as ln


def f(a):
    return (2*a*e**-a+ln(2*a**2))*(2*a**2-3*a-5)


# Implementing Bisection Method
def bisection(x0, x1, w):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > w

    print('\nRequired Root is : %0.8f' % x2)


# Input Section
x0 = input('First Guess: ')
x1 = input('Second Guess: ')
w = input('Tolerable Error: ')

# Converting input to float
x0 = float(x0)
x1 = float(x1)
w = float(w)

# Note: You can combine above two section like this
# x0 = float(input('First Guess: '))
# x1 = float(input('Second Guess: '))
# e = float(input('Tolerable Error: '))


# Checking Correctness of initial guess values and bisecting
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again')

bisection(x0, x1, w)
