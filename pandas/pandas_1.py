import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

###lab1
xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx)

grupa = df.groupby(["Rok"]).agg({"Liczba":["sum"]})

wykres = grupa.plot()
wykres.set_ylabel("Liczba urodzonych")
wykres.set_xlabel("Rok")
wykres.legend()
plt.title("Liczba urodzonych w danym roku")
plt.show()

###lab2
xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx)
print(df)

grupa=df.groupby(["Plec"]).agg({"Liczba":["sum"]})
wykres = grupa.plot.bar()
wykres.set_ylabel('Liczba urodzen')
wykres.set_xlabel('Plec')
wykres.legend()
plt.title('ilosc urodzen wzgledem plci')
plt.show()

###lab3
xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx)
print(df)

grupa=df[(df.Rok>=2012)&(df.Rok<=2017)].groupby(["Plec"]).agg({"Liczba":["sum"]})
wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%')
plt.title('ilosc urodzonych M i K w ost.5 latach')
plt.show()

###lab4
df = pd.read_csv("iris.data", sep=",", names=["Sepal length", "Sepal width", "Petal length", "Petal width", "Class"])

df_1 = df[df["Class"] == "Iris-setosa"]
df_2 = df[df["Class"] == "Iris-versicolor"]
df_3 = df[df["Class"] == "Iris-virginica"]

s_1 = plt.scatter(df_1["Sepal length"], df_1["Sepal width"], color="r")
s_2 = plt.scatter(df_2["Sepal length"], df_2["Sepal width"], color="g")
s_3 = plt.scatter(df_3["Sepal length"], df_3["Sepal width"], color="b")

plt.ylabel("Sepal length")
plt.xlabel("Sepal width")
plt.title("Sepal for each class")
plt.legend((s_1, s_2, s_3), ("Iris-setosa", "Iris-versicolor", "Iris-virginica"), title="Classes")

plt.show()
###lab5
df = pd.read_csv('zamówienia.csv',sep=";")
print(df)

grupa = df.groupby(['Sprzedawca'])["idZamowienia"].count()
print(grupa)
wykres = grupa.plot.bar()
wykres.set_ylabel('Mld')
wykres.set_xlabel('Kontynent')
wykres.legend()
plt.title('Populacja z podziałem na kontynenty')
plt.show()
