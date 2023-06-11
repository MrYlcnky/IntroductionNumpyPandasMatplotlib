import numpy as np
import pandas as pd

maasSozluk={"Isim": ["Ahmet","Mehmet","Ali","Veli"],
            "Departman": ["Yazılım", "Satıs", "Pazarlama","Yazılım"],
            "Maas": [200,300,400,500]
            }

maasDataFrame=pd.DataFrame(maasSozluk)


print(maasDataFrame["Departman"].unique())
print(maasDataFrame["Departman"].nunique())
print(maasDataFrame["Departman"].value_counts())

def bruttenNete(maas):
    return maas*0.66

print(maasDataFrame["Maas"].apply(bruttenNete))
print(maasDataFrame.isnull())

yeniBirVeri={"Karakter Sınıfı":["South Park","South Park","Simpson","Simpson","Simpson"],
             "Karakter Ismi": ["Cartman","Kenny","Homer","Bart","Bart"],
             "Karakter Yas" : [9,10,30,50,10]
             }

karakterDF=pd.DataFrame(yeniBirVeri)

print(karakterDF.pivot_table(values="Karakter Yas",index=["Karakter Sınıfı","Karakter Ismi"]
                             ,aggfunc=np.sum)) #ortalama ya da toplar