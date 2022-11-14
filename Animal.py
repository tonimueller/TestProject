# Deine the general class Animal

class Animals:

    def __init__(self, name):
        self.name = name
        self.size = 0
        self.age = 0

    def print_name(self):
        print(self.name)

    def print_size(self):
        print(f'The animal, {self.name}, is of size {self.size}cm.')

    def print_age(self):
        print(f'The animal, {self.name}, is {self.age} years old.')

    def set_size(self, size ):
        self.size = size

    def set_age(self, age):
        self.age = age

    def increment_age(self):
        self.age += 1
