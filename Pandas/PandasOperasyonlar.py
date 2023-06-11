import numpy as np
import pandas as pd

sozlukVerisi = {"Istanbul": [30, 29, np.nan], "Ankara": [20, np.nan, 25], "Izmir": [40, 39, 38]}
havaDurumuDataFrame = pd.DataFrame(sozlukVerisi)
print(havaDurumuDataFrame)
print(havaDurumuDataFrame.dropna(axis=1))

yeniVerisi = {"Istanbul": [30, 29, np.nan], "Ankara": [20, np.nan, 25], "Izmir": [40, 39, 38],
              "Antalya": [45, np.nan, np.nan]}
yeniDataFrame = pd.DataFrame(yeniVerisi)
print(yeniDataFrame)
print(yeniDataFrame.dropna(axis=1, thresh=2))

print(yeniDataFrame.fillna(20))

# Groupby
maasSozlugu = {"Departman": ["Yazılım", "Yazılım", "Pazarlama", "Pazarlama", "Hukuk", "Hukuk"],
               "Calısan Ismı": ["Ahmet", "Mehmet", "Atil", "Buse", "Fatma", "Burak"],
               "Maas": [100, 150, 200, 300, 400, 500]
               }
maasDataFrame = pd.DataFrame(maasSozlugu)
print(maasDataFrame)

gruoObjesi = maasDataFrame.groupby("Departman")
print(gruoObjesi.count())
print("Mean")
print(gruoObjesi.mean(1))    #ortalama hesaplar
print(gruoObjesi.describe())