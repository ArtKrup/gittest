class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return print('Run!')

    def jump(self):
        return print('Jump!')

    def birthday(self):
        self.age += 1

    def sleep(self):
        return print('Zzzz')


class Dog(Pet):

    def bark(self):
        return print('Bark!')


class Cat:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return print('Run!')

    def jump(self):
        return print('Jump!')

    def birthday(self):
        self.age += 1

    def sleep(self):
        return print('Zzzz')

    def meow(self):
        return print('Meow!')

class Parrot:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return print('Run!')

    def jump(self):
        return print('Jump!')

    def birthday(self):
        self.age += 1

    def sleep(self):
        return print('Zzzz')

    def fly(self):
        return print('Krrrrrr!')


dog1 = Dog('bob', 9, 'art')
print(dog1.name, dog1.master, dog1.age)
dog1.birthday()
dog1.bark()
dog1.sleep()
print(dog1.age)