class SalaryMonthModel:

    def __init__(self, amount, insurance_model, salary_year_model, year):
        self.amount = amount
        self.insurance_model = insurance_model
        self.ndfl_rate = salary_year_model.NDFL_RATE[year]

        self.salary_year_model = salary_year_model

        self.year = year

        self._y = None
        self._w = None
        self._n = None
        self._r = None
        self._z = None

    def __dict__(self):
        return {
            'y': self.y,
            'z': self.z,
            'tax': self.tax,
        }

    def _y_before_limit(self):
        return round(self.amount / (1 + sum(self.insurance_model.rates)), 2)

    def _y_after_limit(self):
        insurance_rate_from = self.insurance_model.after_limit['rate_from']
        insurance_from = self.insurance_model.after_limit['from']
        insurance_fixed = self.insurance_model.after_limit['fixed']

        return (self.amount - (insurance_rate_from * (self.salary_year_model.y - insurance_from)) - insurance_fixed
                + self.salary_year_model.w) / (1 + insurance_rate_from + self.insurance_model.rates[1])

    @property
    def y(self):
        if self._y is None:
            if self.salary_year_model.y >= self.insurance_model.after_limit.get('mode_from'):
                self._y = self._y_after_limit()
            else:
                self._y = self._y_before_limit()

                if (self._y + self.salary_year_model.y) > self.insurance_model.after_limit.get('mode_from'):
                    self._y = self._y_after_limit()

        return self._y

    def _w_before_limit(self):
        return round(self.y * self.insurance_model.rates[0], 2)

    def _w_after_limit(self, mode):
        insurance_rate_from = mode['rate_from']
        insurance_from = mode['from']
        insurance_fixed = mode['fixed']

        return insurance_rate_from * (self.salary_year_model.y + self.y - insurance_from) + \
               insurance_fixed - self.salary_year_model.w

    @property
    def w(self):
        if self._w is None:
            if self.salary_year_model.y + self.y >= self.insurance_model.after_limit.get('mode_from'):
                self._w = self._w_after_limit(self.insurance_model.after_limit)

            if self._w is None:
                self._w = self._w_before_limit()

        return self._w

    @property
    def n(self):
        if self._n is None:
            self._n = round(self.y * self.ndfl_rate, 2)
        return self._n

    @property
    def r(self):
        if self._r is None:
            self._r = round(self.y * self.insurance_model.rates[1], 2)
        return self._r

    @property
    def z(self):
        if self._z is None:
            self._z = round(self.y - self.n, 2)
        return self._z

    @property
    def tax(self):
        return self.w + self.n + self.r
