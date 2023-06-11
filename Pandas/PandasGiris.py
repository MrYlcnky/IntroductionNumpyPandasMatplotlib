import numpy as np
import pandas as pd

#           Series/Seriler
print("Seriler")

myDict={"mehmet": 50, "buse": 40, "Fatma": 30}
print(pd.Series(myDict))

myAge =[50,40,30]
myName=["Mehmet","Buse","Fatma"]
print(pd.Series(myAge))
print(pd.Series(data=myAge,index=myName))

numpyDizisi=np.array([50,40,30])
print(pd.Series(numpyDizisi,myName))

print(pd.Series(["Mehmet","Ahmet","Osman"],[1,2,3]))

yarismaSonucu1=pd.Series([10,5,1],["Mehmet","Ahmet","Osman"])
yarismaSonucu2=pd.Series([20,15,8],["Mehmet","Ahmet","Osman"])

sonSonuc=yarismaSonucu1+yarismaSonucu2
print(sonSonuc)