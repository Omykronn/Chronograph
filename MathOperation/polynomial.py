class Monomial:
    def __init__(self, p: int, c: float):
        self.power = p if p >= 0 else 0
        self.coefficient = c

    def __str__(self, var="x"):
        return "{coeff}*{var}**{p}".format(coeff=self.coefficient, p=self.power, var=var)

    def derive(self):
        return Monomial(self.power - 1, self.coefficient * self.power)


class Polynomial:
    def __init__(self, data, var: str):
        self.variable = var
        self.terms = []

        if type(data) == str:
            for m in data.replace(" ", "").split("+"):
                coeff, power = 1, 0

                if var not in m:
                    coeff = float(m)
                else:
                    power = 1

                    for n in m.split(var):
                        n = n.replace("**", "")

                        if "*" in n:  # Coefficient
                            coeff = float(n.replace("*", ""))
                        elif n != "":  # Power
                            power = int(n)

                self.terms.append(Monomial(power, coeff))
        elif type(data) == list:
            self.terms = data

    def __str__(self):
        return "+".join([m.__str__(self.variable) for m in self.terms])

    def derive(self):
        return Polynomial([n.derive() for n in self.terms], self.variable)

    def format(self):
        carac = [("**3+", "³+"), ("**2+", "²+"), ("**1", ""), ("*" + self.variable + "**0", ""), ("**", "^"), ("*", "×")
                 , ("+-", "-")]
        s = str(self)

        for c in carac:
            s = s.replace(c[0], c[1])

        return s
