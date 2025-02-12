from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
import os

def print_hi(name):
    print(f'Hi, {name}')
    print(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))


if __name__ == '__main__':
    print_hi(f'{os.name}')
    calculate_salary()
    get_employees()


