# guess_the_number_1-100
Мини проект по окончанию курса: "Угадайка чисел"
1. Заголовок программы
2. Функция проверки корректности введенных данных

Теск кейс функции
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

3. Основной цикл программы
4. Сравнение введенного числа с загаданным
5. Улучшение программы добавлением счётчика попыток 