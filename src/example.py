from abc import ABCMeta

class Bidule:

    def __init__(self):
        self.truc = 0

class User(Bidule, metaclass=ABCMeta):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."