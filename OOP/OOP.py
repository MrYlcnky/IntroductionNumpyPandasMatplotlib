# sınıf
myList = list()


# instance & attribute

class SuperKahraman():
    ozelGuc = " "

    def __init__(self, isimInput, yasInput, meslekInput):
        print("init çağrıldı")
        self.isim = isimInput
        self.yas = yasInput
        self.meslek = meslekInput

    def ornekMethod(self):
        print(f"Ben süperkahramanım ve mesleğim: {self.meslek}")


superman = SuperKahraman("Superman", 30, "Gazeteci")
superman.ozelGuc = "Uçabiliyor"
print(superman.ornekMethod())


class Kopek():
    yilCarpani = 7

    def __init__(self, age=5):
        self.age = age

    def insanYasiniHesapla(self):
       return self.age * Kopek.yilCarpani


mydog = Kopek()
print(mydog.age)
print(mydog.insanYasiniHesapla())

