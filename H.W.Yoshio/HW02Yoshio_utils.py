from faker import Faker
import pandas as pd
import requests


### 01 utils ###
def read_requirements_txt() -> str:
    with open('requirements.txt') as my_txt:
        result01 = my_txt.read()
    return result01


### 02 utils ###
def generate_users(how_many=100) -> str:
    fake = Faker('jp_JP')
    new_list = []
    for _ in range(how_many):
        content = fake.name() + ' ' + fake.email()
        new_list.append(content)
    result02 = str(new_list)
    return result02


### 03 utils ###
def read_the_csv() -> dict:
    df = pd.read_csv('hw (2) (1).csv', index_col=0)
    my_list = []
    content = df.mean()
    my_list.append(content)
    result03 = dict(my_list)
    return result03


### 04 utils ###
def read_the_json() -> dict:
    r = requests.get('http://api.open-notify.org/astros.json')
    result04 = r.json()
    return result04