import numpy as np
import matplotlib.pyplot as plt


numpyDizisi1 = np.linspace(0, 10, 12)
numpyDizisi2 = numpyDizisi1 ** 2

(benimFigur,benimEksen)=plt.subplots()

benimEksen.plot(numpyDizisi1,numpyDizisi2,"r")
benimEksen.plot(numpyDizisi2,numpyDizisi1,color="#3A95A8")

(benimFigur2,benimEksen2)=plt.subplots()
benimEksen2.plot(numpyDizisi1,numpyDizisi1+2,"r",linewidth=3)
benimEksen2.plot(numpyDizisi1,numpyDizisi1+4,"r",linestyle="--",marker="o",markerfacecolor="b")
plt.show()
#scatter
plt.scatter(numpyDizisi1,numpyDizisi2)
plt.show()
#histogram
yeniDizi=np.random.randint(0,100,50)
plt.hist(yeniDizi)
plt.show()
#booxplot
plt.boxplot(yeniDizi)
plt.show()