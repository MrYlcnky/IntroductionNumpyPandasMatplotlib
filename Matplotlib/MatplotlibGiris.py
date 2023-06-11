import numpy as np
import matplotlib.pyplot as plt



yasList = [10, 20, 30, 30, 30, 40, 50, 60, 70, 75]
kiloList = [20, 60, 80, 85, 86, 87, 70, 90, 95, 90]

numpyYasList = np.array(yasList)
numpyKiloList = np.array(kiloList)

plt.plot(numpyYasList, numpyKiloList, "g")  # "g" çizgi rengi
plt.xlabel("Yas")
plt.ylabel("Kilo")
plt.title("Kilo'nun Yaşa Göre Değişim Grafiği")
# plt.show()

numpyDizisi1 = np.linspace(0, 10, 12)
numpyDizisi2 = numpyDizisi1 ** 3
plt.plot(numpyDizisi1, numpyDizisi2, "r*-")
# plt.show()

plt.subplot(1, 2, 1)  # 1 sıra olacak 2 kolon olacak 1. grafik
plt.plot(numpyDizisi1, numpyDizisi2, "b*-")
plt.subplot(1, 2, 2)
plt.plot(numpyYasList, numpyKiloList, "y--")
# plt.show()


benimFigure=plt.figure()
figureAxes = benimFigure.add_axes([0.1,0.1,0.3,0.3])
figureAxes.plot(numpyDizisi1,numpyDizisi2,"g")
figureAxes.set_xlabel("X ekseni Veri İsmi")
figureAxes.set_ylabel("Y ekseni Veri İsmi")
figureAxes.set_title("Grafik Başlığı")

fig2=plt.figure()
eksen1=fig2.add_axes([0.1,0.1,0.9,0.9])
eksen2=fig2.add_axes([0.3,0.5,0.3,0.3])

eksen1.plot(numpyDizisi1,numpyDizisi2,"g")
eksen1.set_xlabel("X ekseni ")
eksen1.set_ylabel("Y ekseni ")
eksen1.set_title("Ana Grafik Başlık")

eksen2.plot(numpyDizisi2,numpyDizisi1,"b")
eksen2.set_xlabel("X ekseni ")
eksen2.set_ylabel("Y ekseni ")
eksen2.set_title("Kücük Grafik Başlık")

(benimFigure,benimEksenler)=plt.subplots(nrows=1,ncols=2)

for eksen in benimEksenler:
    eksen.plot(numpyDizisi1,numpyDizisi2,"y")
    eksen.set_xlabel("X Ekseni")

plt.tight_layout()

yeniFigur=plt.figure(dpi=100) #piksel çözünürlük
yeniEksen=yeniFigur.add_axes([0.1,0.1,0.9,0.9])
yeniEksen.plot(numpyDizisi1,numpyDizisi1 ** 2,label="numpyDizisi ** 2")
yeniEksen.plot(numpyDizisi1,numpyDizisi1 ** 3,label="numpyDizisi ** 3")
yeniEksen.legend(loc=2)

yeniFigur.savefig("benimfigur.png",dpi=500)

plt.show()
