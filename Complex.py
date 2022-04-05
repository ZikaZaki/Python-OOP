"""
    This is a class for explaining operator overloading
    ********************************************************
    *    Operator	            Method                     *
    ********************************************************
    *        +	        __add__ (self, other)              *
    *        -	        __sub__ (self, other)              *
    *        /	        __truediv__ (self, other)          *
    *        *	        __mul__ (self, other)              *
    *        <	        __lt__ (self, other)               *
    *        >	        __gt__ (self, other)               *
    *        ==	        __eq__ (self, other)               *
    *        !=	        __ne__ (self, other)               *
    *        <=	        __le__ (self, other)               *
    *        >=	        __ge__ (self, other)               *
    *        **	        __pow__ (self, other)              *
    *        //	        __floordiv__ (self, other)         *
    *        %	        __mod__ (self, other)              *
    *        in	        __contains__ (self, other)         *
    *       not in	    __not_contains__ (self, other)     *
    *        &	        __and__ (self, other)              *
    *        |	        __or__ (self, other)               *
    *        ^	        __xor__ (self, other)              *
    *        <<	        __lshift__ (self, other)           *
    *        >>	        __rshift__ (self, other)           *
    *                                                      *
    ********************************************************
    
"""


class Complex:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):  # overloading the `+` operator
        temp = Complex(self.real + other.real,
                       self.imaginary + other.imaginary)
        return temp

    def __sub__(self, other):  # overloading the `-` operator
        temp = Complex(self.real - other.real,
                       self.imaginary - other.imaginary)
        return temp


obj1 = Complex(3, 7)
obj2 = Complex(2, 5)

obj3 = obj1 + obj2
obj4 = obj1 - obj2

print("real of obj3:", obj3.real)
print("imaginary of obj3:", obj3.imaginary)
print("real of obj4:", obj4.real)
print("imaginary of obj4:", obj4.imaginary)
