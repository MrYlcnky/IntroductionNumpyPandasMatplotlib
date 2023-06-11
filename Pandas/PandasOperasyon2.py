import pandas as pd
import numpy as np

sozluk1={"Isim":["Ahmet","Mehmet","Ali","Veli"],
         "Spor":["Koşu","Yüzme","Koşu","Basketbol"],
         "Kalori":[100,200,300,400]
         }
dataFrame1= pd.DataFrame(sozluk1)
print(dataFrame1)

sozluk2={"Isim":["Buse","Fatma","Ozmen","Kaya"],
         "Spor":["Koşu","Yüzme","Koşu","Basketbol"],
         "Kalori":[200,300,600,500]
         }
dataFrame2=pd.DataFrame(sozluk2,index=[4,5,6,7])

sozluk3={"Isim":["Ayşe","Mahmut","Hızır","Filiz"],
         "Spor":["Koşu","Yüzme","Batminton","tenis"],
         "Kalori":[400,500,700,800]
         }
dataFrame3=pd.DataFrame(sozluk3,index=[8,9,10,11])
print("Concatenation")
#concatenation

print(pd.concat([dataFrame1,dataFrame2,dataFrame3]))

#Merge birleştirme

mergeSozluk4={"Isim":["Ahmet","Mehmet","Ali","Veli"],
         "Spor":["Koşu","Yüzme","Koşu","Basketbol"]
         }
mergeDataFrame4=pd.DataFrame(mergeSozluk4)

mergeSozluk5={"Isim":["Ahmet","Mehmet","Ali","Veli"],
         "Kalori":[100,200,300,400]
         }
mergeDataFrame5=pd.DataFrame(mergeSozluk5)

print(pd.merge(mergeDataFrame4,mergeDataFrame5,on="Isim"))
