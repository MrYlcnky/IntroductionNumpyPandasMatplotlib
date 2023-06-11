
class Meyve():
    def __init__(self,isim,kalori):
        self.isim=isim
        self.kalori=kalori
    def __str__(self):
        return f"{self.isim} şu kadar kaloriye sahiptir: {self.kalori}"
muz=Meyve("Muz",150)
print(muz)

elma=Meyve("Elma",200)
print(elma)