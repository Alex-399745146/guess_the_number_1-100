import random

def is_valid(x):
    if x.isalnum():
        if x.isdigit():
            x = int(x)
            if 1 <= x <= 100:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def test_is_valid(n):
    for _ in range(5):
        n = str('')
        for i in range(random.randint(1, 2)):
            n += str(chr(random.randint(48, 70)))
            if is_valid(n) == True:
                print('Корректные_данные     ===>', n)
            else:
                print('Не_корректные_данные  ===>', n)

n = 1

test_is_valid(n)