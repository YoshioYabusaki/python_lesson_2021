# print("Hello World") # stdout
# inpt = input() #stdin
# print(inpt)

from flask import Flask, request
from datetime import datetime
from utils import generate_password as gp
from utils import read_requirements_txt

app = Flask(__name__)

@app.route('/hello/')
def hello_world():
    return 'Hello, World!'

@app.route('/generate-password/')
def generate_password():

    # validate password-len from client
    password_len = request.args.get('password-len')

    if not password_len:
        password_len = 10
    else:
        if password_len.isdigit():
            password_len = int(password_len)
            # 10...50
        else:
            password_len = 10
            # return 'Invalid parameter password-len. Should be int.'

    password = gp(password_len)
    return f'{password}\n'


@app.route('/requirements/')
def requirements():
    result = read_requirements_txt()
    return result




if __name__ == '__main__':
    app.run(host='0.0.0.0')

print(123456)

#
# """"
# http://google.com/search/?name=hillel&city=Dnepr
#
# http:// - protocol (https)
# """