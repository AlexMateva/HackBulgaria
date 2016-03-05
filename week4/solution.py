import sys


class Polynom:
    def __init__(self, string):
        self.string = string
        self.power = {
        }

    def set_the_power(self):
        temp = self.string.split("+")
        for coef in temp:
            t = coef.split('^')
            if len(t) == 2:
                self.power[int(t[1])] = 0
            elif len(t) == 1:
                if "x" in t[0]:
                    self.power[1] = 0
                else:
                    self.power[0] = 0

        return self.power

    def remove_emptyspace(self):
        self.set_the_power()
        temp = self.string.split(" ")
        result = ''
        if len(temp) != 1:
            for x in temp:
                result += x
            self.string = result

    def set_the_coeff(self):
        self.remove_emptyspace()
        self.set_the_power()
        temp = self.string.split("+")
        for coef in temp:
            t = coef.split('^')
            if len(t) == 2:
                if len(t[0]) == 1:
                    self.power[int(t[1])] = self.power[int(t[1])] + 1
                else:
                    self.power[int(t[1])] = self.power[int(t[1])] + int(coef[0])
            elif len(t) == 1:
                if "x" in t[0]:
                    coef = t[0].split("x")
                    if len(t[0]) == 1:
                        self.power[1] = 1
                    elif len(t[0]) > 1:
                        self.power[1] = self.power[1] + int(coef[0])
                else:
                    self.power[0] += int(t[0])
        return self.power

    def polynom_to_string(self):
        result = ''
        self.set_the_power()
        self.set_the_coeff()
        p = list(self.power.keys())
        length = len(p)

        for x in reversed(p):
            length -= 1
            if x > 1:
                if self.power[x] != 1:
                    result += str(self.power[x])
                    result += 'x^'
                else:
                    if result != '':
                        result += 'x^'
                    else:
                        result += 'x^'
                result += str(x)
                if length > 0:
                    result += ' + '
            elif x == 1:
                if self.power[x] != 1:
                    result += str(self.power[x])
                    result += 'x'
                else:
                    if result != '':
                        result += 'x'
                    else:
                        result += 'x'
                if length > 0:
                    result += ' + '
            elif x == 0:
                if self.power[x] != 0:
                    result += str(self.power[x])
                else:
                    result = result[::-1]
                    result = result[3:]
                    result = result[::-1]
        self.string = result


class Derivates:
    def __init__(self, polynom):
        polynom.set_the_coeff()
        self.polynom = polynom
        self.old_powers = list(polynom.power.keys())
        self.compress_polynom = []
        self.new_powers = {
        }

    def __str__(self):
        polynom.polynom_to_string()
        return "The derivative of f(x) = {} is:\nf'(x) = {}".format(self.polynom.string, self._derivate_to_string())

    def _derivate_to_string(self):
        result = ''
        self.derivate_powers()
        p = list(self.new_powers.keys())
        length = len(p)

        if 'x' not in polynom.string:
            result = '0'
        else:
            for x in reversed(p):
                length -= 1
                if x > 1:
                    result += str(self.new_powers[x])
                    result += 'x^'
                    result += str(x)
                    if length > 0:
                        result += ' + '
                elif x == 1:
                    result += str(self.new_powers[x])
                    result += 'x'
                    if length > 0:
                        result += ' + '
                elif x == 0:
                    result += str(self.new_powers[x])
        return result

    def derivate_powers(self):
        for x in self.old_powers:
            if x > 0:
                self.new_powers[x-1] = polynom.power[x] * x
        return self.new_powers

a = sys.argv[1]
polynom = Polynom(a)
derivate = Derivates(polynom)
print(derivate)
