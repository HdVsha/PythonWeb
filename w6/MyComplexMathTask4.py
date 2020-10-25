#from MyMathTask3 import MyMath --- thought to import the class, but the task wanted another
import cmath
import math


class MyMath:

    pi = 3.14
    _complex = False   # Инкапсуляция(сделали приватное поле)

    @staticmethod
    def sin(x):
        return math.sin(x)

    @classmethod
    def get_complex(cls):
        return cls._complex

    @classmethod
    def sqrt(cls, x):
        if cls.get_complex() is True:  # Полиморфизм, потому что используем разные результаты
            result = cmath.sqrt(x)
            return result.real, result.imag
        else:
            if x < 0:
                raise ValueError("What are you doing with negative number in this class!")
            else:
                return math.sqrt(x)


class MyComplexMath(MyMath):  # Наследование
    _complex = True


cl1 = MyMath()
cl = MyComplexMath()
print(cl1.sqrt(1))
print(cl.sqrt(1))
print(cl.sqrt(-1))
print(cl1.sqrt(-1))

