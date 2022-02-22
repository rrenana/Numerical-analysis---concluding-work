from datetime import datetime
#the team:Michal Teneboim,Renana Ziner,Noa Asulin


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
            print("the solutions for gouse is:", q)
            print("Intermediate solutions:\n",arrx)
            print(arry)
            print(arrz)



a = [0.04,0.01,-0.01,0.06]
b=[0.2,0.5,-0.2,0.3]
c=[1,2,4,11]
gauss(a,b,c)

approx = gauss(a,b,c)
date = datetime.now()
d = date.day
hour = date.hour
minute = date.minute
print('the answer is:', format(approx)+"00000"+format(d)+format(hour)+format(minute))
