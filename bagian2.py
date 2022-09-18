
class kocheng:

    #nyoba constructor
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color = color

a = kocheng("meng",10)
a.set_color(20)
print(a.name)
print(a.color)