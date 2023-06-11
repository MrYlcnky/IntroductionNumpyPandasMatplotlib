import numpy as np
import pandas as pd

data = np.random.randn(4, 3)
print(data)

dataFrame = pd.DataFrame(data)
print(dataFrame)

yeniDataFrame = pd.DataFrame(data, index=["Mehmet", "Buse", "Fatma", "Yalçın"],
                             columns=["Maas", "Yas", "Calisma Saatleri"])
print(yeniDataFrame)
print(yeniDataFrame["Yas"])
print(yeniDataFrame["Calisma Saatleri"])
print(yeniDataFrame[["Maas", "Yas"]])
print("-------")
print(yeniDataFrame.loc["Mehmet"])
print("*****************************")
print(yeniDataFrame.iloc[2])

yeniDataFrame["Emeklilik Yasi"] = yeniDataFrame["Yas"] + yeniDataFrame["Yas"]  # ekleme
print(yeniDataFrame)

print(yeniDataFrame.drop("Emeklilik Yasi", axis=1, inplace=True))  # silme     inplace: yerinde kesin siler kaldırır
print(yeniDataFrame < 0)
print(yeniDataFrame[yeniDataFrame < 0])

# index değiştirme
print("Reset")
print(yeniDataFrame.reset_index())

yeniIndexList = ["Meh", "Bus", "Fat", "Yal"]
yeniDataFrame["Yeni Indeks"] = yeniIndexList
print(yeniDataFrame)
yeniDataFrame.set_index("Yeni Indeks", inplace=True)
print(yeniDataFrame)

print("Multi Indeks")  # Multi İndeks

ilkIndeksler = ["Simpson", "Simpson", "Simpson", "South Park", "South Park", "South Park"]
icIndeksler = ["Homer", "Bart", "Marge", "Cartman", "Kenny", "Kyle"]
birlesmisIndex = list(zip(ilkIndeksler, icIndeksler))
print(birlesmisIndex)

birlesmisIndex = pd.MultiIndex.from_tuples(birlesmisIndex)
print(birlesmisIndex)

benimCizgiFilmListem = [[10, "A"], [20, "B"], [30, "C"], [40, "D"], [50, "E"], [60, "F"]]
cizgiFilmNumpyDizisi = np.array(benimCizgiFilmListem)
cizgiFilmDataFrame = pd.DataFrame(cizgiFilmNumpyDizisi, index=birlesmisIndex, columns=["Yas", "Meslek"])
print(cizgiFilmDataFrame)

print(cizgiFilmDataFrame.loc["Simpson"].loc["Marge"])
cizgiFilmDataFrame.index.names=["Film Adı", "İsim"]
print(cizgiFilmDataFrame)
