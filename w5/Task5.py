class Mother:
    _name = "who?"

    def __init__(self, name):
        self._name = name

    def get_name_len(self):
        return len(self._name)

    def get_str(self):
        return f"Name: {self._name}\n"

    def __str__(self):
        return self.get_str()

class Daughter(Mother):
    __mother = "who?"

    def __init__(self, name, mother):
        super().__init__(name)
        self.__mother = mother

    def get_str(self):
        return f"Name: {self._name}, Mother: {self.__mother}\n"

    def __str__(self):
        return self.get_str()

    def get_name_len(self):
        print("Daughter's length of name is:")
        return len(self._name)


if __name__ == "__main__":
    m = Mother("Alice")
    d = Daughter("Alice", "Katya")
    print(m)
    print(d)
