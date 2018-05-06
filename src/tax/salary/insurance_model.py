class InsuranceModel:
    BEFORE_LIMIT = {
        2009: [0.26, 0.002],

        2014: [0.3, 0.002],
        2015: [0.3, 0.002],
        2016: [0.22, 0.085],
        2017: [0.22, 0.085],
        2018: [0.22, 0.085]
    }

    AFTER_LIMIT = {
        2014: {
            'rate_from': 0.1,
            'from': 624000,
            'fixed': 187200,
            'mode_from': 520000

        },
        2015: {
            'rate_from': 0.1,
            'from': 624000,
            'fixed': 187200,
            'mode_from': 520000
        },
        2016: {
            'rate_from': 0.1,
            'from': 796000,
            'fixed': 175120,
            'mode_from': 718000
        },
        2017: {
            'rate_from': 0.1,
            'from': 876000,
            'fixed': 192720,
            'mode_from': 718000
        },
        2018: {
            'rate_from': 0.1,
            'from': 1021000,
            'fixed': 224620,
            'mode_from': 718000
        }
    }

    def __init__(self, year):
        """
        :param rates:
        """
        self.rates = self.BEFORE_LIMIT[year]
        self.after_limit = self.AFTER_LIMIT[year]
