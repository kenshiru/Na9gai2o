class DividendsMonthModel:

    rates = {
        # YEAR: [profit_tax_rate, dividends_tax_rate]
        2014: [0.2, 0.09],
        2015: [0.2, 0.09],
        2016: [0.2, 0.13],
        2017: [0.2, 0.13],
        2018: [0.2, 0.13]
    }

    def __init__(self, year, amount):
        self.year = year
        self.amount = amount

    def __dict__(self):
        return {
            'y': self.y,
            'z': self.z,
            'tax': self.tax,
        }


    @property
    def y(self):
        return self.amount

    @property
    def t(self):
        return self.rates[self.year][0] * self.y

    @property
    def d(self):
        return self.rates[self.year][1] * self.y

    @property
    def z(self):
        return self.y * (1 - self.rates[self.year][0]) * (1 - self.rates[self.year][1])

    @property
    def tax(self):
        return self.y * (self.rates[self.year][0] + self.rates[self.year][1] * (1 - self.rates[self.year][0]))

