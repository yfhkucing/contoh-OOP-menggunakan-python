#class attributes lesson idk
class employee:
    #tidak berubah utk setiap objek
    number_of_employee = 0

    def __init__(self,name,age):
        #object attribute uses self
        #berubah utk setiap objek
        self.name = name
        self.age = age

p1 = employee("budi",29)
p2 = employee("bambang",25)

print(p1.number_of_employee)
#bisa diubah dengan menggunakan nama kelas
employee.number_of_employee = 8

print(p1.number_of_employee)