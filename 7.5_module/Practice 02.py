class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)

sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 37, 68, 95)

#...........2............
oldest = max([sakib, musfiq, kamal, jack, kalam], key=lambda player: player.age)
print(f"The oldest cricketer is: {oldest.name}, Age: {oldest.age}")

#..........4...........    
class Student:
    def __init__(self, name):
        self.__name = name  # private

    def get_name(self):       # getter
        return self.__name

    def set_name(self, name):  # setter
        if name != "":
            self.__name = name

s = Student("Rafi")
print(s.get_name())   # Rafi
s.set_name("Tanvir")
print(s.get_name())   # Tanvir


#.........5.......
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def start_car(self):
        self.engine.start()

my_car = Car()
my_car.start_car()  # Output: Engine started
