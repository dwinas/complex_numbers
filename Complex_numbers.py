import math

class Complex:
    def __init__(self, real, imag):
        self._real =real
        self._imag = imag

    def __str__(self):
        real = f"{self._real:.2f}"
        imag = f"{self._imag:.2f}"
        if self._imag == 0:
            return f"{real}+0.00i"
        elif self._real == 0: 
            sign = "-" if self._imag <0 else "+"
            return f"0.00{sign}{imag}i"
        else:
            sign = "-" if self._imag < 0 else "+"
            return f"{real}{sign}{imag}i"

    

    


    def __add__(self, other):
        return Complex(self._real + other._real, self._imag + other._imag)





def main():

    a = Complex(2,1)
    b = Complex(5,6)

    print(a+b)
    








if __name__ =="__main__":
    main()