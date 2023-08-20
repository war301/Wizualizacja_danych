import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt
import random
import numpy.random

###lab1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
print(df)
#df.to_excel('z_indeksami.xlsx',  sheet_name='Wydatki z indeksami')

print(df[(df.Liczba > 1000)])
print(df[(df.Imie == "ARKADIUSZ")])
print(df[(df.Rok==2000)].agg({'Liczba':['sum']}))
print("------")
for x in range(6):
    print(df[(df.Rok==2000+x)].agg({'Liczba':['sum']}))
print("------")    
print(df[(df.Plec=="M")].agg({'Liczba':['sum']}))
print(df[(df.Plec=="K")].agg({'Liczba':['sum']}))     
for x in range(6):
    print(df[(df.Rok==2000+x)&(df.Plec=="M")].head(1))
    print(df[(df.Rok==2000+x)&(df.Plec=="K")].head(1))

###lab2
df = pd.read_csv('zamówienia.csv',sep=";")
print(df)
print(df["Sprzedawca"].unique())

print(df.nlargest(5,["Utarg"]))

print(df.groupby("Sprzedawca")["idZamowienia"].count())
print(df.groupby("Kraj")["idZamowienia"].count())
print(df[((df["Data zamowienia"].str.contains("2005")) & (df["Kraj"] == "Polska"))]["idZamowienia"].count())
print(df[df["Data zamowienia"].str.contains("2004")]["Utarg"].mean())
print(df[df["Data zamowienia"].str.contains("2004")].to_csv("zamowienia_2004.csv", index=False, sep=";"))

###lab3
df=pd.read_csv("zamówienia.csv",sep=";")
print(df)
cos1=df["Sprzedawca"].unique()
cos=pd.DataFrame(cos1)
print(cos)
print(df.nlargest(5,"Utarg"))

###test
df = pd.read_csv('zamówienia.csv',sep=";")
print(df)

df["data"]=pd.to_datetime(df['Data zamowienia'])
df["Rok"],df["Miesiac"]=df["data"].dt.year,df["data"].dt.month
print(df["Rok"])

plt.axis([0,20,-1.5,1.5])
x=np.arange(0,21,0.1)
y=-(np.sin(x))
plt.plot(x,np.cos(x),'b',label="f(x)=cos(x)")
plt.plot(x,y,'y--',label="f(x)=-sin(x)")
plt.legend()
plt.show()

print(df.nlargest(5,["Utarg"]))
