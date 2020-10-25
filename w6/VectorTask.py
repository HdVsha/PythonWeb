import math
import numpy as np


class Vector:
    __x = 0
    __y = 0
    __z = 0
    __values = [__x, __y, __z]

    def __init__(self, *args):
        if len(args) == 0:
            pass
        elif type(args[0]) == str:  # [0] Because python has to know that it is a string
            self.__values = list(map(float, list(args[0].split(','))))
        else:
            self.__values = list(args)

    def __add__(self, other):
        added = list(a + b for a, b in zip(self, other))
        return Vector(*added)

    def __iter__(self):   # Have to redefine it in order to use zip
        return self.__values.__iter__()

    def __sub__(self, other):
        subbed = list(a - b for a, b in zip(self, other))  # Функция zip позволяет пройтись одновременно
        return Vector(*subbed)                             # по нескольким итерируемым объектам

    def length_of_vector(self):
        return math.sqrt(sum(value**2 for value in self.__values))  # I don't know why __len__ can't return the same val

    def __and__(self, other):  # Thought it was suitable to use numpy in that case
        a = np.array(self.__values)
        b = np.array(other.__values)
        return np.cross(a, b)

    def scal_mul(self, other):  # Our dot product (скалярное произведение)
        return sum(a * b for a, b in zip(self, other))

    def __mul__(self, other):
        if type(other) == type(self):  # Have to check the types ir order
            return self.scal_mul(other)  # not to implicitly change the types( int to float)
        elif type(other) == int or type(other) == float:
            product = list(a * other for a in self)
            return Vector(*product)

    def __str__(self):
        return f"[{self.__values[0]}, " + f"{self.__values[1]}, " + f"{self.__values[2]}]" + "\n"


if __name__ == "__main__":
    a = Vector(1, 2, 3)
    b = Vector('4, 5, 6')

    print(a)
    print(b)

    print(f"Sum = {a + b}")
    print(f"Dot product = {a * b}")
    print(f"Cross product = {a & b}")
    print(f"Subtraction product = {a - b}")
    print(f"Length of the vector a = {a.length_of_vector()}")

    N = int(input())
    vector_list = []

    for t in range(N):
        temp = input()
        temp = ','.join(list(temp.split(' ')))
        vector_list.append(Vector(temp))

    mx = Vector()

    for vector in vector_list:
        mx = Vector()
        if vector.length_of_vector() > mx.length_of_vector():
            mx = vector

    print(mx)