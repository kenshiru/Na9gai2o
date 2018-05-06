import flask
from flask import request
from tax.salary import year_salary_calc
from tax.dividends import year_dividends_calc

app = flask.Flask(__name__, template_folder='./templates/')


@app.route('/', methods=['GET'])
def index():
    return flask.render_template('index.html')


@app.route('/api/calc', methods=['POST'])
def calc_salary():
    incomming_data = request.get_json(force=True)
    year = int(incomming_data.get('year'))
    salary_amount_list = incomming_data.get('monthly_salaries_list')

    salary_month_models_generator = year_salary_calc(year, salary_amount_list)
    dividends_month_models_generator = year_dividends_calc(year, salary_amount_list)
    response = flask.jsonify(
        success=True,
        data={
            'year': year,
            'salaries': [model.__dict__() for model in salary_month_models_generator],
            'dividends': [model.__dict__() for model in dividends_month_models_generator]
        }
    )
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


app.run(host='0.0.0.0', port=30001)
