
class Elma():
    def __init__(self,isim):
        self.isim=isim

    def bilgiVer(self):
        return self.isim + " 100 kaloridir "

class Muz():
    def __init__(self,isim):
        self.isim=isim

    def bilgiVer(self):
        return self.isim + " 150 kaloridir "


elma = Elma("elma")
elma.bilgiVer()

muz = Muz("Muz")
muz.bilgiVer()

meyveList=[elma,muz]

for meyve in meyveList:
    print(meyve.bilgiVer())