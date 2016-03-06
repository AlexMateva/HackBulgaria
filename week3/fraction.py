class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        if self.numerator == 0:
            return "{}".format(int(self.numerator))
        elif self.numerator == self.denominator:
            return "{}".format(int(self.numerator))
        elif self.denominator == 1:
            return "{}".format(int(self.numerator))
        else:
            return "{} / {}".format(int(self.numerator), int(self.denominator))

    def __repr__(self):
        return self.__str__()

    def _cancel_fraction(self):
        for x in range(2, int(max(self.denominator, self.numerator))):
            while self.numerator % x == 0 and self.denominator % x == 0:
                self.numerator = self.numerator / x
                self.denominator = self.denominator / x
        return self.__str__()

    def __add__(self, other):
        num = self.numerator * other.denominator + self.denominator * other.numerator
        denom = self.denominator * other.denominator
        return Fraction(num, denom)._cancel_fraction()

    def __sub__(self, other):
        if self._cancel_fraction() == other._cancel_fraction():
            return 0
        else:
            num = self.numerator * other.denominator - self.denominator * other.numerator
            denom = self.denominator * other.denominator
            return Fraction(num, denom)._cancel_fraction()

    def __mul__(self, other):
        num = self.numerator * other.numerator
        denom = self.denominator * other.denominator
        return Fraction(num, denom)._cancel_fraction()

    def __eq__(self, other):
        return self._cancel_fraction() == other._cancel_fraction()
