from datetime import datetime

def interpulation(a,b):

    f=a[0]+a[1]*b+a[2]*b*b
    return f

def gauss(t1, t2, t3):
    arrx=[]
    arry=[]
    arrz=[]
    x = 0
    y = 0
    z = 0
    error = 0
    t = 0
    while error == t:
        x1 = (t1[3] - t1[1] * y - t1[2] * z)/t1[0]
        x2 = (t2[3] - t2[0] * x1 - t2[2] * z)/t2[1]
        x3 = (t3[3] - t3[0] * x1 - t3[1] * x2)/t3[2]
        if abs(x-x1)!=error or abs(y-x2)!= error  or abs(z-x3)!=error:
            x = x1
            y = x2
            z = x3
            arrx.append(x)
            arry.append(y)
            arrz.append(z)
        else:
            t = 1
            q = (x1, x2, x3)
            return q



a = [1,2,4,0]
b=[1,2.25,2.25*2.25,0.112463]
c=[1,2.3,5.29,0.167996]
y=gauss(a,b,c)
x=2.4
print("The results obtained after activating Gauss:",y)
print("the final solution is:",interpulation(y,x))
approx = round(interpulation(y,x),6)
date = datetime.now()
d = date.day
hour = date.hour
minute = date.minute
print('the answer is:', format(approx)+"00000"+format(d)+format(hour)+format(minute))