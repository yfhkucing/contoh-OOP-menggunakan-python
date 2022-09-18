#coba inheritance
x = int(5)#input("masukkan angka pertama = ")
y = int(3)#input("masukkan angka kedua = ")
print(str(x))
print(str(y))
class option:
    def __init__(self,name):
        self.name = print(name)
        #self.x = x
        #self.y = y


class operasi1(option):

    def tambah(self):
        return x+y
    def kurang(self):
        return x-y
    def kali(self):
        return x*y
    def bagi(self):
        return x/y

class operasi2(option):

    def modullo(self):
        return x//y
    def remaider(self):
        return x%y


p1 = operasi1("kurang")
print(p1.kurang())
p2 = operasi2("remaider")
print(p2.remaider())