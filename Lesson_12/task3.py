"""
Fraction
Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *) with appropriate
checking and error handling
"""

class Fraction:
    def __init__(self, value):
        try:
            self.numerator, self.denominator = value.as_integer_ratio()
        except AttributeError:
            print('Value mast be int or float')
        
    def __str__(self):
        return f'{self.__class__.__name__}({self.numerator}, {self.denominator})'
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.numerator}, {self.denominator})'
    
    def __add__(self, other):
        return Fraction((self.numerator * other.denominator + other.numerator * self.denominator) /
                        (self.denominator * other.denominator))
    
    def __sub__(self, other):
        return Fraction((self.numerator * other.denominator - other.numerator * self.denominator) /
                        (self.denominator * other.denominator))
    
    def __truediv__(self, other):
        if self.denominator * other.numerator == 0:
            raise ZeroDivisionError
        else:
            return Fraction((self.numerator * other.denominator) / (self.denominator * other.numerator))
    
    def __mul__(self, other):
        return Fraction((self.numerator * other.numerator) / (self.denominator * other.denominator))


x = Fraction(1/2)
y = Fraction(1/4)

print(x + y)  # == Fraction(3, 4)

