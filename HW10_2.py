def unique_content(original):

    marker = 0
    try:
        if type(original) != list:
            print(type(original))
            raise TypeError

        try:
            for i in original:
                if type(i) == int or type(i) == float:
                    marker = 1
                else:
                    marker = 0
                    raise Exception  #TypeError
        except Exception:  #TypeError:
            print("Error: list contains not numerical symbols")

    except TypeError:
        print("Error: type 'list' required")

    if marker == 1:
        unique = set(original)
        if len(unique) == len(original):
            print('There are no duplicates on the list')
        else:
            print('There are duplicates on the list')


# spisok = 11
# spisok = "AADD"
# spisok = {'a' : 1, 'b' : 2}
# spisok = [12, 1, 56]
# spisok = [12, 'A', 14, 16, 12, 32, 'B', 3]
spisok = [12, 23.3, 14.4, -16, 12, 32, 8]
unique_content(spisok)

