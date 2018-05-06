import os
from tax.salary import year_salary_calc
from tax.dividends import year_dividends_calc

args = os.sys.argv
year = int(args[1])
salary_amount_list = [int(100000) for i in range(12)]

salary_month_models_generator = year_salary_calc(year, salary_amount_list)
dividends_month_models_generator = year_dividends_calc(year, salary_amount_list)

s_total = 0
s_tax_total = 0

d_total = 0
d_tax_total = 0

for i in range(12):
    s_model = next(salary_month_models_generator)
    s_total += s_model.z
    s_tax_total += s_model.tax

    d_model = next(dividends_month_models_generator)
    d_total += d_model.z
    d_tax_total += d_model.tax


print('TOTAL SALARY   : Z=%s, TAX=%s' % (s_total, s_tax_total))
print('TOTAL DIVIDENDS: z=%s, TAX=%s' % (d_total, d_tax_total))
