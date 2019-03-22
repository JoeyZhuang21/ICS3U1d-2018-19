

def caught_speeding(speed, is_birthday):

    if (60 >= speed and not is_birthday) or (65 >= speed and is_birthday):
        return 0
    elif ((61 <= speed and speed <= 80) and not (is_birthday)) or ((66 <= speed and speed <= 85) and (is_birthday)):
        return 1
    else:
        return 2

print(caught_speeding(65, True))