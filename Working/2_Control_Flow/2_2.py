

def date_fashion(you, date):

    if 8 <= you or 8<= date:
        return 2
    elif 2 >= you or 2 >= date:
        return 0
    else:
        return 1

print(date_fashion(5, 5))