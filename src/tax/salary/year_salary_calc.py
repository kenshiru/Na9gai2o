from . import SalaryMonthModel, SalaryYearModel, InsuranceModel
import logging

logging.basicConfig(level=logging.DEBUG)


def year_salary_calc(year, salary_monthly_list):
    salary_year_model = SalaryYearModel()
    for month_number, monthly_salary_amount in enumerate(salary_monthly_list):
        salary_month_model = SalaryMonthModel(amount=monthly_salary_amount, insurance_model=InsuranceModel(year),
                                              salary_year_model=salary_year_model, year=year)

        logging.info('[S]%s:  Y=%s, Z=%s, TAX=%s' %
                     (month_number + 1, round(salary_month_model.y), round(salary_month_model.z), round(salary_month_model.tax)))
        yield salary_month_model
        salary_year_model.add_to_y(salary_month_model.y, month_number + 1)
        salary_year_model.add_to_w(salary_month_model.w, month_number + 1)




