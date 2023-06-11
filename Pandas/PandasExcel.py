import numpy as np
import pandas as pd

dataFrame=pd.read_excel("maas.xlsx")
print(pd.read_excel("maas.xlsx"))

doluDegerlerDF=dataFrame.dropna()

doluDegerlerDF.to_excel("yenimaas.xlsx") #yeni excel oluşturur
