class OptionError(Exception):
    def __init__(self, message):
        self.message = message

class AgeError(Exception):
    def __init__(self, message = '   Error!'):
        self.message = message
    def f(self, n):
        print(self.message)
        if about.get(n) is not None:
            print(about.get(n))
        if law.get(n) is not None:
            print(law.get(n))
        if phone.get(n) is not None:
            print('Contact us for more information: ', phone.get(n))


def service_choice():
    print('Hello! Choose an option:')
    print('   1 - applying for unemployment benefits', '\n   2 - applying for pension')
    option = -1
    a = int(input('Enter 1 or 2: '))
    try:
        if a < 1 or a > 2:
            raise OptionError('Incorrect input')
    except OptionError as oer:
        print(oer)
    else:
        option = a
    return option

def year_input():
    year = int(input('Enter year of your birth: '))
    try:
        if year < 1923 or year > 2023:
            raise AgeError
    except AgeError as aer:
        aer.f(0)
    return year


about = {0: "incorrect year", 1: "you can't apply for unemployment benefits", 2: "you can't apply for pension"}
law = {1: 'Applying is possible at age over 18', 2: 'Applying is possible at age over 60'}
phone = {1: '808 22 33 4444', 2: '808 55 66 7777'}

option = service_choice()
if option != -1:
    birth_year = year_input()

if option == 1:
    try:
        if 2023 > birth_year > 2005:
            raise AgeError('    Sorry,')
    except AgeError as aer:
        aer.f(1)
    else:
        if phone.get(1) is not None:
            print('Contact us for more information: ', phone.get(1))

if option == 2:
    try:
        if 2023 > birth_year > 1963:
            raise AgeError('   Sorry,')
    except AgeError as aer:
        aer.f(2)
    else:
        if phone.get(2) is not None:
            print('Contact us for more information: ', phone.get(2))




