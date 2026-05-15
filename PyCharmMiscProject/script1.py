#class Hero:
    # Конструктор класса
#    def __init__(self,name,level,hp):
        # Атрибуты класса
#        self.name = name
#        self.level = level
 #       self.hp = hp


# объект\экземпляр на основе класса
#Kirito = Hero("Kirito",100,1000)

#print(Kirito.name)
#print(Kirito.level)
#print(Kirito.hp)


class MyInt:
    def __int__(self,value):
        self.value = value

    def __str__(self):
        return str(self. value)

MyInt = MyInt(123)
py_int = 123
my_list = list([1,2,3,45])
my_tuple = tuple([1,2,3,45])

print(my_tuple.count(1))
print(my_list.reverse())
