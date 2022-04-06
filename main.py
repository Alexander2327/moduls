from application.salary import colculate_salary
from application.db.people import get_employees
from datetime import date

if __name__ == '__main__':
    colculate_salary()
    get_employees()
    print(date.today().strftime("%d-%m-%Y"))