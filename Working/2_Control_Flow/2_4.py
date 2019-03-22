

def squirrel_play(temp, is_summer):
    if (60 <= temp and temp <= 90) and not is_summer:
        return True
    elif (60 <= temp and temp <= 100) and is_summer:
        return True
    else:
        return False

print(squirrel_play(95, True))