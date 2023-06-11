import numpy as np

#    Numpy array
print("Array")
myList= [20,30,40]
print(np.array(myList))

matrixList=[[10,20,30],[20,30,40],[30,40,50]]
print(np.array(matrixList))

#---         Methodlar         ----#

print("Arange")
#   Arange (range )
print(np.arange(0,20,2))
np.zeros((2,2))  # 2 ye 2 sıfırlardan oluşan matrix
np.ones((3,3))      # 3 e 3 birlerden oluşan matrix

print("Linspace")
#linspace
print(np.linspace(0,20,6))  # 0 ile 20 arasında 6 tane sayı arasındaki farklar eşit

print("Eye")
#eye
print(np.eye(3)) #matris oluşturur köşeden köşeye 1 ler var

print("Random")
#random
print(np.random.randn(4,4))   # 4 e 4 lük matrix random sayılar
np.random.randn(4)            # 4 random sayı
np.random.randint(1,10,3)       # 1 den 10 arası 3 tane random tam sayı

#               Numpy Dizi Methodları
print("Numpy Dizi Methodları")
myNumpyDizim = np.arange(30)

print(myNumpyDizim.reshape(5,6))
print(myNumpyDizim.max())
print(myNumpyDizim.min())
print(myNumpyDizim.argmax())
print(myNumpyDizim.argmin())
