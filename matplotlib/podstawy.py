import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlrd
import openpyxl
import random

###lab1
x = np.arange(1, 21)

plt.plot(x, 1/x, label="f(x)=1/x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.xlim(1,len(x))
plt.ylim(0,1)
plt.show()
###lab2
x = np.arange(1, 21)

plt.plot(x, 1/x, "g>:", label="f(x)=1/x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.ylim(0,1)
plt.title("Wykres funkcji f(x) dla x [1, 20]")
plt.show()

# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
###lab3
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30.1, 0.1)
s = np.sin(x)
c = np.cos(x)

plt.plot(x, s, "b", label="sin(x)")
plt.plot(x, c, "c", label="cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Wykres funkcji sin(x) i cos(x) dla x [0, 30]")
plt.show()
###lab4
x = np.arange(0, 30.1, 0.1)
s1 = np.sin(x) + 2
s2 = np.sin(x) * -1

plt.plot(x, s1, "#1872b1", label="sin(x)")
plt.plot(x, s2, "#ff861b", label="sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend(loc="center left")
plt.title("Wykres sin(x), sin(x)")
plt.show()
###lab5
df = pd.read_csv("iris.data", sep=",", names=["Sepal length", "Sepal width", "Petal length", "Petal width", "Class"])

data = {
    "a": df["Sepal length"],
    "b": df["Sepal width"],
    "c": np.random.randint(0, 50, 150)
}
data["d"] = np.abs(data["a"] - data["b"])

plt.scatter("a", "b", c="c", s="d", data=data)
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.show()
###lab6
###lab7
xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx, index_col=None)

dane_wykres_1 = df.groupby("Plec")["Liczba"].sum().reset_index()
dane_wykres_2 = df.groupby(["Plec", "Rok"])["Liczba"].sum().reset_index()
dane_wykres_2_K = dane_wykres_2[dane_wykres_2["Plec"] == "K"].reset_index()
dane_wykres_2_M = dane_wykres_2[dane_wykres_2["Plec"] == "M"].reset_index()
dane_wykres_2 = df.groupby(["Plec", "Rok"])["Liczba"].sum().reset_index()
dane_wykres_3 = df.groupby("Rok")["Liczba"].sum().reset_index()

plt.subplot(131)
plt.bar(dane_wykres_1["Plec"], dane_wykres_1["Liczba"], color=["orange", "yellow"])
plt.xlabel("Plec")
plt.ylabel("Liczba urodzonych")

plt.subplot(132)
plt.plot(dane_wykres_2_K["Rok"], dane_wykres_2_K["Liczba"])
plt.plot(dane_wykres_2_M["Rok"], dane_wykres_2_M["Liczba"])

plt.xlabel("Rok")
plt.ylabel("Liczba urodzonych")

plt.subplot(133)
plt.bar(dane_wykres_3["Rok"], dane_wykres_3["Liczba"], color="c")
plt.xlabel("Rok")
plt.ylabel("Liczba urodzonych")

plt.suptitle("Liczba urodzonych K i M")

plt.show()
###lab8
def rzucaj(n):
    wynik = []
    for i in range(n):
        wynik.append(random.randint(1,6) + random.randint(1,6))
    plt.hist(wynik, bins=2, facecolor='g', alpha=0.75, density=True)
    plt.xlabel('Suma rzutów')
    plt.ylabel('Prawdopodobieństwo')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()

rzucaj(1000)
###lab9
df = pd.read_csv("zamowienia.csv", sep=";")

dane = df.groupby("Sprzedawca")["Utarg"].sum().reset_index()

explode = [0 for i in range(len(dane["Sprzedawca"]))]
explode[random.randint(0, len(dane["Sprzedawca"]) - 1)] = 0.3

plt.figure(figsize=(7,5))
wedges, texts, autotexts = plt.pie(dane["Utarg"], labels=dane["Sprzedawca"],
    autopct=lambda pct: "{:.2f}%".format(pct), textprops=dict(color="black"), shadow=True, explode=explode)
plt.setp(autotexts, size=12, weight="bold")
plt.title("Procent udziałów sprzedawców")
plt.legend(title="Sprzedawcy", bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0.)
plt.show()
###lab10
###test
x1 = np.arange(0.0, 2.0, 0.02)
x2 = np.arange(0.0, 2.0, 0.02)

y1 = np.sin(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x2)


plt.subplot(2, 1, 1)
plt.plot(x1, y1, '-')
plt.title('Dwa podwykresy')
plt.ylabel('sin(x)')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'r-')
plt.xlabel('x')
plt.ylabel('cos(x)')

plt.show()
