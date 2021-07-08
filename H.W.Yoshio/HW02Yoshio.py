from flask import Flask, request
from HW02Yoshio_utils import read_requirements_txt
from HW02Yoshio_utils import generate_users
from HW02Yoshio_utils import read_the_csv
from HW02Yoshio_utils import read_the_json

app = Flask(__name__)


### 01 ###
@app.route('/requirements/')
def requirements():
    result_01 = read_requirements_txt()
    return result_01


### 02 ###
# without validation → http://127.0.0.1:5000/generate-users/?how-many=100
@app.route('/generate-users/')
def the_generated_users():
    how_many = int(request.args.get('how-many'))
    result_02 = generate_users(how_many)
    return result_02


### 03 ###
@app.route('/mean/')
def mean_calculation():
    dict_item = read_the_csv()

    list_of_the_key = dict_item.keys()
    list_of_the_key = list(list_of_the_key)
    float_height = float(list_of_the_key[0])

    list_of_the_value = dict_item.values()
    list_of_the_value = list(list_of_the_value)
    float_weight = float(list_of_the_value[0])

    # изменение единиц
    new_height = float_height * 2.54
    new_weight = float_weight * 0.453592

    result_03 = {'Height(cm)': new_height, 'Weight(kg)': new_weight}
    return result_03


### 04 ###
@app.route('/space/')
def number_of_astronauts():
    the_json = read_the_json()

    the_number = the_json["number"]
    result_04 = {'The current number of astronauts': the_number}
    return result_04


if __name__ == '__main__':
    app.run(host='0.0.0.0')