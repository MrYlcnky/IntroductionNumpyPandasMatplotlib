
class Animal():

    def __init__(self):
        print("hayvan sınıfı init")
    def method1(self):
        print("hayvan sınıfı method1")
    def method2(self):
        print("hayvan sınıfı method2")

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Kedi sınıfı initi çağrıldı")
    def miyavla(self):
        print("miyav")
        #override
    def method1(self):
        print("kedi sınıfı methodu 1")

myAnimal=Animal()
myCat=Cat()

# kedi sınıfı hayvandan methodlar kullana bilir çünkü miras bırakıldı ama hayvan sınıfı kedi sınıfından bir şey kullanılmaz
myCat.method1()
myCat.miyavla()
myAnimal.__init__()
#üstüne yazma override
