#belajar inheritance
#2 class/ lebih yg hampir sama
#constructor atau method yg sama ditulis di class yang berbeda

#general class (parent?)
class pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"i am {self.name} and i am {self.age} years old")

#specific class(child?)
class kocheng(pet) :

    def __init__(self,name,age,color):
        #super merujuk kepada class pet
        #tulis yg mau di pass dari parent aja
        super().__init__(name,age)
        self.color = color

    def sound(self):
        print("meong")

class segawon(pet) :
    def sound(self):
        print("bark")

p = kocheng("meng",5,"hitam")
p.sound()
p.show()
