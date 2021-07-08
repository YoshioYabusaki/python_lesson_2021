import random
import string


def generate_password(password_len=10) -> str:
    if not isinstance(password_len, int):
        raise TypeError('Invalid Type...')

    choices = string.ascii_letters + string.digits + string.punctuation
    result = ''

    for _ in range(password_len):
        result += random.choice(choices)

    return result



def read_requirements_txt() -> str:
    with open('requirements.txt') as my_txt:
        content = my_txt.read()
    return content


