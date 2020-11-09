import math


class Complex:

    def __init__(self, r=0, im=0):
        self.__real = r
        self.__imag = im

    def __add__(self, other):
        return Complex(self.__real + other.__real, self.__imag + other.__imag)

    def __sub__(self, other):
        return Complex(self.__real - other.__real, self.__imag - other.__imag)

    def __mul__(self, other):
        return Complex(self.__real * other.__real -
                       self.__imag * other.__imag,
                       self.__real * other.__imag +
                       self.__imag * other.__real)

    def __truediv__(self, other):
        div = other.__real ** 2 + other.__imag ** 2
        if div == 0:
            return None
        else:
            return Complex(
                (self.__real * other.__real +
                 self.__imag * other.__imag)/div,
                (self.__imag * other.__real -
                 self.__real * other.__imag)/div)

    def squared_parts(self):
        return self.__real ** 2 + self.__imag ** 2

    def abs(self):
        return math.sqrt(self.squared_parts())

    def __neg__(self):
        return Complex(-self.__real, -self.__imag)

    def __pow__(self, other):
        try:
            z_abs = self.abs()
            z_angle = math.atan(self.__imag/self.__real)
            real_part = z_abs * math.cos(z_angle * other)
            imag_part = z_abs * math.sin(z_angle * other)
            return Complex(int(real_part), int(imag_part))
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot pow the complex number with 0 real part")

    def __str__(self):
        return f"{self.__real} + " + f"{self.__imag}" + "j" + "\n"  # I am cautious with "f"-strings

    def get_real(self):
        return self.__real

    def get_imag(self):
        return self.__imag

# if __name__ == "__main__":
#
#     a = Complex(5, 12)
#     b = Complex(3, 4)
#     print(a)
#     print(a ** 3)
#     print(a + b)
#     print(a - b)
#     print(a / b)
#     print(a * b)
#     print(a.abs())