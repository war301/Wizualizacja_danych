import numpy as np
###lab1
a=np.arange(4)
b=np.array([0,1])
print(a)
print(a.shape)
print(a.ndim)
print(b)
c=a.astype('float')
print(c)
m = np.array([np.arange(2), np.arange(2)])
print(m)
print(type(m))

n=np.arange(2,21*2,2)
print(n)
print(len(n))
###lab2
a=np.arange(2,10,1.5,float)
print(a)
b=a.astype(int)
print(b)
###lab3
def funkcja(n):
    a=np.arange(1,n*n+1,1)
    print(a)

funkcja(5)   
###lab4
def funkcja(x,ile):
    z=np.logspace(1,ile,num=ile,base=x)
    z=z.astype(int)
    print(z)

funkcja(2,4)
###lab5
def funkcja(n):

    mat_diag = np.diag([x for x in range(n,0,-1) ])
    print(mat_diag)

funkcja(3)    
###lab6
marcin = 'piestłbgagojkjct'
mar_3 = np.array(list(marcin))
mar_3=mar_3.reshape((4,4))
print(mar_3)
###lab7
n=6
def funkcja(n):
    srodek=np.diag([2 for x in range(n)])
    for x in range(1,n,1):
        gorny_rog=np.diag([2**(1+x) for n in range(n-x) ],x)
        srodek=srodek+gorny_rog
    for x in range(1,n,1):
        gorny_rog=np.diag([2**(1+x) for n in range(n-x) ],-x)
        srodek=srodek+gorny_rog    
    print(srodek) 
funkcja(n)       
###lab8
print("1=pionowo,0=poziomo")
mat=np.arange(36).reshape(6,6)
print(mat)
kier=int(input())
def funkcja(mat,kier):
    (wymiar,wymiar1)=mat.shape
    pol=int(wymiar/2)
    if wymiar%2==0:
        if kier==1:
                print(mat[:, 0:pol])
        else:
            for x in range(pol):
                print(mat[:, x])       
    if wymiar%2==1:
        print("nie można rozwiązać")
funkcja(mat,kier)
###lab9
def fibo(n ):
    if n>2:
        mlode, dorosle = 1, 0
        tab=[0]
        for _ in range(n):
            mlode, dorosle = dorosle, dorosle + mlode
            tab.append(dorosle)
        return tab        
    elif n==1:
        return [0,1]
    elif n==2:
        return [0,1,1]    
    elif n==0:
        return [0]


mar_3 = np.array(list(fibo(24)))
mar_3=mar_3.reshape((5,5))
print(mar_3)
