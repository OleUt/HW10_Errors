def month_name(number):

    year = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
            7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

    status = 0
    try:
        number = int(number)
    except:
        month = 'Sorry, the symbol is not integer'
        status = 1
    finally:
        if status == 0:
            try:
                if year.get(number) is not None:
                    month = year.get(number)
                else:
                    raise KeyError
            except KeyError:
                month = 'Sorry, the number is out of range'

    return month


month_number = input("Enter month number: ")
print(month_name(month_number))

