from Animal import  Animals

class Mammal(Animals):

    def __init__(self, mammal_name):
        super().__init__( mammal_name)
        self.time = 0

    def set_lactation_time(self, time):
        self.time = time

    def print_lactation_Time(self):
        print(f'The mammal, {self.name}, feeds its childs {self.time} months.')
