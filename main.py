import random
num = (random.randint(1, 100))    # num = рандомное число 1-100
#print(num)
print('Добро пожаловать в числовую угадайку')
def is_valid(x):    # обьявление функции проверки вводимых данных (защита от дурака т.н.)
    if x.isalnum():    # проверяем наличие буквенно-цифровых символов в веденных данных
        if x.isdigit():    # определяет наличие цифровых символов
            x = int(x)
            if 1 <= x <= 100:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
n = str('')
counter = -1
while n != num:
    counter += 1
    n = str(input('Угадай целое число от 1 до 100:'))
    if is_valid(n):
        n = int(n)
        if n > num:
            print('Слишком много, попробуйте еще раз')
        elif n < num:
            print('Слишком мало, попробуйте еще раз')
        else:
            print('Вы угадали, поздравляем! C', counter, '-ой попытки.')
            break
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')