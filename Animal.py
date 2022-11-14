# Deine the general class Animal

class Animals:

    def __init__(self, name):
        self.name = name
        self.size = 0

    def print_name(self):
        print(self.name)

    def add_size(self, size ):
        self.size = size