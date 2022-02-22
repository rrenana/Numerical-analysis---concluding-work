#Neville Method
#Noa Asulin , Michal Tenenboim, Renana Zinner
from datetime import datetime

def Neville_Algorithm(xm, ym, xn, yn, x):
    p = ((x - xm)*yn - (x-xn)*ym) / (xn-xm)
    return p

def main ():
    # Table points
    x0 = 2
    y0 = 0
    x1 = 2.25
    y1 = 0.112463
    x2 = 2.3
    y2 = 0.167996
    x3 = 2.7
    y3 = 0.222709

    # Finding the value of the function at a given point
    x = 2.4

    #calculation
    p01 = round(Neville_Algorithm(x0, y0, x1, y1, x), 6)
    p12 = round(Neville_Algorithm(x1, y1, x2, y2, x), 6)
    p23 = round(Neville_Algorithm(x2, y2, x3, y3, x), 6)
    p02 = round(Neville_Algorithm(x0, p01, x2, p12, x), 6)
    p13 = round(Neville_Algorithm(x0, p12, x2, p23, x), 6)
    p03 = round(Neville_Algorithm(x0, p02, x2, p13, x), 6)
    print("The result of a 1st order polynomial consisting of points x0,y0,x1,y1 is:", p01)
    print("The result of a 1st order polynomial consisting of points x1,y1,x2,y2 is:", p12)
    print("The result of a 1st order polynomial consisting of points x2,y2,x3,y3 is:", p23)
    print("The result of a  2nd order polynomial consisting of points x0,y0,x1,y1,x2,y2 is:", p02)
    print("The result of a  2nd order polynomial consisting of points x1,y1,x2,y2,x3,y3 is:", p13)
    print("The result of a  3nd order polynomial consisting of points x0,y0,x1,y1,x2,y2,x3,y3 is:", format(p03)+"00000"+format(d)+format(hour)+format(minute))


date = datetime.now()
d = date.day
hour = date.hour
minute = date.minute



main()