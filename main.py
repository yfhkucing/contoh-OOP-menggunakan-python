#belajar OOP
#bikin class
x = int(0)
class kocheng:
    #method adalah function dalam class
    #method menentukan operasi sebuah objek
    def meong(self):
        print("meong")

    def add(self,x):
        return x+1
    #method def_init_ ( constructor)
    #buat ngasih sebuah nilai pada setiap member pada class kalo ada objek yang ditambahkan
    #Constructors are generally used for instantiating an object.
    # The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created.
    # In Python the __init__() method is called the constructor and is always called when an object is created.
    def __init__(self,name):
        self.name = name
        print(name)

kocheng("meng")
kocheng("meong")



