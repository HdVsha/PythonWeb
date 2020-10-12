class Animal:
    _name = "unknown"
    _age = "unknown"
    _type = "unknown"

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_str(self):
        return f"Name = {self._name}, Age = {self._age}\n"

    def __str__(self):
        return self.get_str()

    def type_of_animal(self):
        return self._type

class Zebra(Animal):
    _name = "Marty"
    _age = "18"
    _num_of_lines = -1
    _type = "mammal"

    def __init__(self, name, age, num_of_lines):
        super().__init__(name, age)
        self._num_of_lines = num_of_lines

    def get_str(self):
        return f"Name = {self._name}, Age = {self._age}," \
               f"Number of lines = {self._num_of_lines}," \
               f"Type of animal = {self.type_of_animal()}\n"

    def __str__(self):
        return self.get_str()


class Dolphin(Animal):
    _name = "Morry"
    _age = "16"
    _num_of_partners = -1
    _type = "mammal from water"

    def __init__(self, name, age, num_of_partners):
        super().__init__(name, age)
        self._num_of_partners = num_of_partners

    def get_str(self):
        return f"Name = {self._name}, Age = {self._age}," \
               f" Number of partners = {self._num_of_partners}," \
               f" Type of animal = {self.type_of_animal()}"

    def __str__(self):
        return self.get_str()


if __name__ == "__main__":
    z = Zebra("Kolya", 25, 150)
    d = Dolphin("Dory", 100, 295)

    print(z)
    print(d)
