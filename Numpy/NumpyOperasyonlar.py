import numpy as np

benimDizim= np.arange(0,15)
print(benimDizim[5])
print(benimDizim[3:8])
benimDizim[3:8]=-5      # 3 den 7 ye kadar -5 yazılır
print(benimDizim)

baskaDizi = np.arange(0,24)

slicingDizisi = baskaDizi.copy()
slicingDizisi = slicingDizisi[3:6]
print(slicingDizisi)
print(benimDizim)

#   Matrix
print("Matrix")
matrixList=[[10,20,30],[20,30,40],[30,40,50]]
matrixDizisi= np.array(matrixList)
print(matrixDizisi[1:,2])

#operasyonlar
print("Operasyonlar")

yeniDizi = np.random.randint(1,100,20)
print(yeniDizi)
print(yeniDizi>24)
sonucDizi=yeniDizi>24
print(yeniDizi[sonucDizi])

sonDizi=np.arange(0,24)
print(sonDizi+sonDizi)
print(sonDizi*sonDizi)
print(sonDizi-sonDizi)
print(sonDizi/sonDizi)   # 0/0 da nan yazar
print(np.sqrt(sonDizi)) #karakök
