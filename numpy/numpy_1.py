import numpy as np
###lab1
# inicjujemy dane
a = np.array( [20,30,40,50] )
b = np.arange( 4 )
print(b)
# wykonujemy operację i zapisujemy do nowej zmiennej
c = a-b
print(c)
# wykonujemy operację: kwadrat zawartości
print(b**2)
# możemy również zmodyfikować obecne zmienne
print(a)
a+=b
print(a)
a-=b
print(a)
print("------")
b = np.arange(12).reshape(3,4)
print(b)
# suma całej macierzy
print(b.sum())
# suma każdej z kolumn
print(b.sum(axis=0))
# minimum każdego rzędu
print(b.min(axis=1))
# skumulowana suma dla rzędu
print(b.cumsum(axis=1))
print("------")
# inicjujemy dane
a = np.arange(3)
b = np.arange(3)
print(a.dot(b))  # iloczyn macierzy
print(np.dot(a,b)) # inny sposób
print("------")
# macierz całkowita
a = np.ones(3, dtype=np.int32)
print(a)
print(a.dtype.name)
# macierz zmiennoprzecinkowa
b = np.linspace(0,np.pi,3)
print(b)
print(b.dtype.name)
# wynikiem jest macierz zmiennoprzecinkowa
c = a+b
print(c)
print(c.dtype.name)
# wynikiem jest macierz liczb zespolonych
d = np.exp(c*1j)
print(d)
print(d.dtype.name)


a = np.arange(3)
print(a)
b=np.linspace(1,6,3)
print(b)
c=a.dot(b)
print(c)
print(a*b)

###lab2
mat=np.arange(9).reshape(3,3)
print(mat)
mat1=np.arange(16).reshape(4,4)
print(mat1)
print(mat.min(axis=0))
print(mat1.min(axis=0))
print("-------")
print(mat.min(axis=1))
print(mat1.min(axis=1))
###lab3
a = np.arange(3)
print(a)
b=np.linspace(1,6,3)
print(b)
c=a.dot(b)
###lab4
import math
a=np.array([33,10,2])
b=np.array([-3,np.pi,math.sqrt(9)])

print(a*b)
###lab5
b = np.arange(3)
print(b)
print(np.exp(b))
print(np.sqrt(b))
c = np.array([2., -1., 4.])
print(np.add(b, c))

mat=np.arange(6).reshape(2,3)
print(mat)
a=np.sqrt(mat)
print(a)
###lab6
mat=np.arange(6).reshape(2,3)
print(mat)
b=np.cos(mat)
print(b)
###lab7
mat=np.arange(6).reshape(2,3)
print(mat)
b=np.cos(mat)
print(b)
a=np.sqrt(mat)
print(a)
dod=np.add(a,b)
print(dod)
###lab8
# generujemy macierz 3x2
b = np.arange(6).reshape(3,2)
print(b)
for a in b:
   # iterujemy wzdłuż pierwszej osi
   print(a)

print("-------")
# generujemy macierz 3x2
b = np.arange(6).reshape(3,2)
print(b)
for a in b.flat:
   # iterujemy jakby to była macierz płaska
   print(a)

mat=np.arange(9).reshape(3,3)
for x in mat:
   # iterujemy wzdłuż pierwszej osi
   print(x)

mat=np.arange(9).reshape(3,3)
for x in mat.flat:
   # iterujemy wzdłuż pierwszej osi
   print(x)
###lab9
mat=np.arange(9).reshape(3,3)
for x in mat.flat:
   # iterujemy wzdłuż pierwszej osi
   print(x)
###lab10
# generujemy macierz 1x6
b = np.arange(6)
print(b)
print(b.shape)
# generujemy macierz 3x3
c = np.array([np.arange(3), np.arange(3), np.arange(3)])
print(c)
print(c.shape)
print("--------")
# generujemy macierz 1x6
b = np.arange(6)
print(b)
print(b.shape)
# przeksztalacamy ja na macierz 2x3
c = b.reshape((2,3))
print(c)
print(c.shape)
# przeksztalacamy ja na macierz 3x2
d = c.reshape((3,2))
print(d)
print(d.shape)
# spłaszczamy macierz zyskujac pierwotny kształt ze zmiennej b
e = d.ravel()
print(e)
print(e.shape)
# transpozycja macierzy
f = c.T
print(f)
print(f.shape)
print("--------")
mat=np.arange(64).reshape(1,64)
print(mat)
mat=np.arange(64).reshape(2,32)
print(mat)
mat=np.arange(64).reshape(4,16)
print(mat)
mat=np.arange(64).reshape(8,8)
print(mat)
###lab11
mat=np.arange(12).reshape(3,4)
print(mat)
mat=mat.ravel()
print(mat)
mat=np.arange(12).reshape(4,3)
print(mat)
mat=mat.ravel()
print(mat)
mat=np.arange(12).reshape(2,6)
print(mat)
mat=mat.ravel()
print(mat)


