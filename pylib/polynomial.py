


class Polynomial:

    def __init__(self, *coefficients):
        if len(coefficients) < 1:
            coefficients = [0]
        
        # Remove leading zero coefficients.
        while coefficients[0] == 0 and len(coefficients) > 1:
            coefficients = coefficients[1:]

        # Tuple for immutability.
        self.coefficients = tuple(coefficients)

    def degree(self):
        return len(self.coefficients) - 1

    def __len__(self):
        return len(self.coefficients)

    def __iter__(self):
        yield from self.coefficients

    def terms(self):
        result = []
        exp = self.degree()
        for c in self.coefficients:
            if c != 0:
                result.append(c * x ** exp)
            exp -= 1
        return result

    def __call__(self, x):
        result = 0
        exp = self.degree()
        for c in self.coefficients:
            result += pow(x, exp) * c
            exp -= 1
        return result

    def derivative(self):
        newCoefficients = []
        exp = self.degree()
        # Exclude final constant term
        for c in self.coefficients[:-1]:
            newCoefficients.append(c * exp)
            exp -= 1
        return Polynomial(*newCoefficients)

    def antiderivative(self, constant=0):
        newCoefficients = []
        exp = self.degree()
        for c in self.coefficients:
            newC = c / (exp + 1)
            if newC.is_integer():
                newC = int(newC)
            newCoefficients.append(newC)
            exp -= 1
        newCoefficients.append(constant)
        return Polynomial(*newCoefficients)

    def __add__(self, a):
        if isinstance(a, Polynomial):
            # Add two polynomials
            c1 = [c for c in self.coefficients]
            c2 = [c for c in a.coefficients]
            newCoefficients = []
            # Make sure both coefficient lists match in length
            if len(c1) < len(c2):
                c1 = [0] * (len(c2) - len(c1)) + c1
            elif len(c2) < len(c1):
                c2 = [0] * (len(c1) - len(c2)) + c2
            for i in range(len(c1)):
                newCoefficients.append(c1[i] + c2[i])
            return Polynomial(*newCoefficients)
        else:
            # Add a constant
            newCoefficients = [c for c in self.coefficients]
            newCoefficients[-1] += a
            return Polynomial(*newCoefficients)

    def __sub__(self, a):
        return self.__add__(a * -1)

    def __rsub__(self, a):
        return self.__mul__(-1).__add__(a)

    def __mul__(self, a):
        if isinstance(a, Polynomial):
            # Get a list of terms for each polynomial
            t1 = [(self.coefficients[i], self.degree() - i) for i in range(len(self.coefficients))]
            t2 = [(a.coefficients[i], a.degree() - i) for i in range(len(a.coefficients))]
            # Answer will have degree equal to the sum of the degrees of the operands
            newCoefficients = [0] * (self.degree() + a.degree() + 1)
            # Multiply each term one by one
            for u in t1:
                for v in t2:
                    exp = u[1] + v[1]
                    c = u[0] * v[0]
                    newCoefficients[-(exp + 1)] += c
            return Polynomial(*newCoefficients)

        else:
            # Scale every coefficient
            newCoefficients = [c * a for c in self.coefficients]
            return Polynomial(*newCoefficients)

    def __truediv__(self, a):
        if isinstance(a, Polynomial):
            raise TypeError("Dividing a polynomial by another polynomial is not supported.")
        newCoefficients = [c / a for c in self.coefficients]
        return Polynomial(*newCoefficients)

    def __floordiv__(self, a):
        if isinstance(a, Polynomial):
            raise TypeError("Dividing a polynomial by another polynomial is not supported.")
        newCoefficients = [c // a for c in self.coefficients]
        return Polynomial(*newCoefficients)

    def __xor__(self, a):
        if not isinstance(a, int) or a < 0:
            raise TypeError("Can only raise a polynomial to a positive integer power.")
        if a == 0:
            return Polynomial(1)
        result = self
        for i in range(a - 1):
            result = result * self
        return result

    __rmul__ = __mul__
    __radd__ = __add__
    __pow__ = __xor__

    def __str__(self):
        result = ""
        exp = self.degree()
        for c in self.coefficients:
            if c != 0:
                if hasattr(c, "is_integer") and c.is_integer():
                    c = int(c)
                if result != "":
                    if c > 0:
                        result += " + "
                    else:
                        result += " - "
                        c = -c
                if exp == 0 or c != 1:
                    result += str(c) if c != -1 else "-"
                if exp != 0:
                    result += "x"
                if exp > 1:
                    result += to_superscript(exp)

            exp -= 1

        # Special case: polynomial has all zero coefficients. Show constant term.
        if result == "":
            result = "0"

        return result

    def __repr__(self):
        return str(self)


def to_superscript(n):
    digits = ("⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹")
    result = ""
    for d in str(n):
        result += digits[int(d)]
    return result
    
x = Polynomial(1, 0)


