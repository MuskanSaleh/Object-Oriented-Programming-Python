class Fraction:
    # Constructor
    def __init__(self, n, d):
        if d == 0:
            raise ValueError("Denominator cannot be zero")  # Prevent division by zero
        self.num = n  # Numerator
        self.den = d  # Denominator
        self.simplify()  # Simplify fraction on creation
    
    # Helper method to simplify the fraction
    def simplify(self):
        def gcd(a, b):  # Greatest Common Divisor meeans reduce fraction 4/8 to 1/2
            while b:
                a, b = b, a % b
            return a
        
        common = gcd(self.num, self.den)
        self.num //= common #ensures division of integers
        self.den //= common

    # Magic method for string representation
    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    # Addition of two fractions
    def __add__(self, other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)  # Return new fraction, not string

    # Subtraction of fractions
    def __sub__(self, other):
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)

    # Multiplication of fractions
    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)

    # Division of fractions
    def __truediv__(self, other):
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return Fraction(temp_num, temp_den)

# Testing the Fraction class
x = Fraction(3, 4)
y = Fraction(5, 6)

print("x:", x)
print("y:", y)

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
