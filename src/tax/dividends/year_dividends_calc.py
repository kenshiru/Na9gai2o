from . import DividendsMonthModel
import logging


def year_dividends_calc(year, salary_monthly_list):
    for month_number, monthly_salary_amount in enumerate(salary_monthly_list):
        div_model = DividendsMonthModel(year, monthly_salary_amount)
        logging.info('[D]%s:  Y=%s, Z=%s, TAX=%s' % (month_number + 1, round(div_model.y), round(div_model.z), round(div_model.tax)))
        yield div_model

