class Dog:
    # пробный комментарий

    def __init__(self, height, weight, name, age, master, adress='Minsk'):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__age = age
        self.__master = master
        self.__adress = adress

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def get_master(self):
        return self.__master

    def set_adress(self, new_adress):
        self.__adress = new_adress

    def get_adress(self):
        return  self.__adress


dog1 = Dog('120', '6', 'first', '0.5', 'art', "Gomel")
print(dog1.name)
dog1.name = 'second'
print(dog1.name)



