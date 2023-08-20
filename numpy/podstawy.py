import numpy as np
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
