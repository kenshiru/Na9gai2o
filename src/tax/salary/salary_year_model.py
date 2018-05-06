class SalaryYearModel:
    NDFL_RATE = {
        2014: 0.13,
        2015: 0.13,
        2016: 0.13,
        2017: 0.13,
        2018: 0.13
    }

    def __init__(self):
        self.y_sample = {}
        self.w_sample = {}

    @property
    def y(self):
        return sum(self.y_sample.values())

    @property
    def w(self):
        return sum(self.w_sample.values())

    def add_to_y(self, amount, index):
        self.y_sample[index] = amount

    def add_to_w(self, amount, index):
        self.w_sample[index] = amount
