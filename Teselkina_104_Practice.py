from typing import List, Dict


# 1
def index_(growth: float, weight: float):
    # объявляем функцию с двумя параметрами, котоая вычисляет индекс массиы тела и выводит в кунсоль результат
    index: float = weight / growth ** 2  # переменная, которая ссылается на индекс массы тела
    if index < 16.5:  # условие
        print(f'Ваш индекс массы тела - {index}. Крайний недостаточный вес')
    elif 16.5 < index < 18.4:
        print(f'Ваш индекс массы тела - {index}. Недостаток в весе')
    elif 18.5 < index < 24.9:
        print(f'Ваш индекс массы тела - {index}. Нормальный вес тела')
    elif 25 < index < 30:
        print(f'Ваш индекс массы тела - {index}. Избыточная масса тела')
    elif 30.1 < index < 34.9:
        print(f'Ваш индекс массы тела - {index}. Ожирение 1 степени')
    elif 35 < index < 40:
        print(f'Ваш индекс массы тела - {index}. Ожирение 2 степени - тяжелое')
    elif index > 40:
        print(f'Ваш индекс массы тела - {index}. Ожирение 3 степени - крайне тяжелое')


# 2
def figures(integer: int) -> str:  # объявляем функцию с одним параметром, которая возвращает строку
    if integer == 3:
        return 'треугольник'
    elif integer == 4:
        return 'квадрат / ромб'
    elif integer == 5:
        return 'пятиугольник'
    elif integer == 6:
        return 'шестиугольник (гексагон)'
    elif integer == 7:
        return 'семиугольник (гептагон)'
    elif integer == 8:
        return 'восьмиугольник (октагон)'
    elif integer == 9:
        return 'девятиугольник'
    elif integer == 10:
        return 'десятиугольник (декагон)'
    else:
        return 'введенное число вне диапазона'


# 3
def next_day(day: int, month: str, year: int) -> tuple:  # объявляем функцию с тремя параметрами и выводит кортеж
    leap_year: List[int] = [i for i in range(1904, 3000, 4)]  # список с високосными годами

    if year in leap_year:  # условие
        day_in_month: Dict[str:int] = {'январь': 31, 'февраль': 29, 'март': 31, 'апрель': 30, 'май': 31, 'июнь': 30,
                                       'июль': 31, 'август': 31, 'сентябрь': 30, 'октябрь': 31,
                                       'ноябрь': 30, 'декабрь': 31}
        # словарь, содержащий пары: ключ(месяц) - замок(количество дней)
    else:
        day_in_month: Dict[str:int] = {'январь': 31, 'февраль': 28, 'март': 31, 'апрель': 30, 'май': 31, 'июнь': 30,
                                       'июль': 31,
                                       'август': 31, 'сентябрь': 30, 'октябрь': 31, 'ноябрь': 30, 'декабрь': 31}

    if day < day_in_month[month]:  # условие: если день меньше, чем количество дней в месяце
        return day + 1, month, year  # возвращает день + 1 и неизмененный месяц и год

    elif day == day_in_month[month] and month != 'декабрь':
        # альтернативное условие: если день = количеству дней в месяце (то есть последний) и месяц не декабрь
        list_month: List[str] = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
                                 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
        return 1, list_month[list_month.index(month) + 1], year  # возвращает 1 число, следующий месяц и год

    elif day == day_in_month[month] and month == 'декабрь':  # если день последний и месяц декабрь
        return 1, 'январь', year + 1  # возвращает 1 января следующего года


# 4
def sum_delivery(product: int) -> float:  # объявляем функцию с одним параметром (количество заказанных товаров)
    if product == 1:  # условие: если товар один
        return 10.95  # возвращаем число
    else:  # альтернативное условие (товаров больше одного)
        return 10.95 + 2.95 * (product - 1)  # возвращаем значение выражения


# 5
def fraction(numerator: int, denomenator: int):  # объявляем функцию с двумя параметрами (числитель и знаменатель)
    list_num_denomenator: List[int] = [_ for _ in range(1, denomenator + 1)]
    # переменная, которая ссылается на список чисел от 1 до числителя
    multiplicity_for_numerator = []  # переменная, которая ссылается на пустой список
    for number in list_num_denomenator:  # цикл: для каждого элемента в списке
        if numerator % number == 0 and denomenator % number == 0:
            # если числитель и знаменатель делятся на число без остатка
            multiplicity_for_numerator.append(number)  # добавляем элемент в конец списка
    return numerator / multiplicity_for_numerator[-1], denomenator / multiplicity_for_numerator[-1]
    # возвращаем числитель и знаменатель деленные на последнее число списка


# 6
def work_with_list(my_list: List):  # объявляем функцию с одним параметром
    print(f'{my_list[::-1]} - список в перевернутом виде')
    print(f'{my_list[2:8]} - срез списка')
    print(f'{list(set(my_list))} - список без дубликатов')

    def delete_num(list_without_elem):
        list_without_elem.pop(5)
        print(f"{my_list} - список без 5 элемента")

    delete_num(my_list)

    def sort_list(my_list_1):
        new_list = []
        for elem in my_list_1:
            if type(elem) == int:
                new_list.append(elem)
        new_list.sort()
        print(f'{new_list} - список по возрастанию')
        print(f'{new_list[::-1]} - список по убыванию')

    sort_list(my_list)

    def list_without_num(list_without_numbers):
        list_without_num_ = []
        for i in list_without_numbers:
            if type(i) != int:
                list_without_num_.append(i)
        print(f'{list_without_num_} - список без чисел')

    list_without_num(my_list)


# 7
def cuntRange(any_list: List, min_num: int, max_num: int):  # объявляем функцию с тремя параметрами
    for object_ in any_list:  # цикл: для каждого элемента в списке
        if type(object_) == int:  # если тип объекта - целое число
            interval_int: List[int] = [i for i in range(min_num, max_num + 1)]
            # список, состоящий из элементов от минимального до максимального
            if object_ in interval_int:  # условие: если объект в списке
                print(f'{object_} - {any_list.count(object_)}', end=' ')
                # вывод в кансоль объект и количество его повторений
        elif type(object_) == float:  # если тип объекта - число в плавающей точной
            interval_float: List[float] = [float(i) for i in range(min_num, max_num + 1)]
            # лист состоящий из чисел от минимального до максимального
            if min(interval_float) < object_ < max(interval_float):
                # если число в диапазоне от минимального до максимального
                print(f'{object_} - {any_list.count(object_)}', end=', ')
                # вывод в кансоль числа и количества его повторений


# 8
def count_list_in_list(all_list: List) -> int:
    # объявляем функцию с одним параметом, которая считает количество вложенных списков в списке
    count_lists: int = 0
    for _ in all_list:
        if type(_) == list:
            count_lists += 1
    return count_lists


# 9
def anagram(first_word: str, second_word: str) -> bool:
    # объявляем переменную с двумя параметрами, которая проверяет являются ли слова анаграммами
    if second_word == first_word[::-1]:
        return True
    else:
        return False


# 10
def dict_mobile(string):  # объявляем функцию с одним параметром
    dict_mobile: Dict[int:tuple] = {1: ('.', ',', '?', '!', ':'), 2: ('A', 'B', 'C'), 3: ('D', 'E', 'F'),
                                    4: ('G', 'H', 'I'), 5: ('J', 'K', 'L'), 6: ('M', 'N', 'O'), 7: ('P', 'Q', 'R', 'S'),
                                    8: ('T', 'U', 'V'), 9: ('W', 'X', 'Y', 'Z'), 0: (' ',)}
    # словарь, содержащий пары ключ(цифра в телефоне)-замок(какие символы в нем находятся)
    for letter in string.upper():  # цикл: для каждого элемента в строке (в верхнем регистре)
        for keys, letter_comparison in dict_mobile.items():  # для каждого элемента в паре ключ - значение
            for _ in letter_comparison:  # цикл: для каждого элемента в кортеже значений
                if letter == _:  # если буква в строке = букве в картеже
                    print(str(keys) * (letter_comparison.index(_) + 1), end='')
                    # вывод в кансоль ключа умноженного на индекс символа + 1


# 11
def flattering(data_list: List) -> list:  # объявляем функцию с одним параметром
    l_1 = []  # переменная, которая ссылается на пустой список
    while data_list:  # цикл: пока в списке есть элементы
        elem = data_list.pop()  # удаляем последний элемент в списке и присваиваем его переменной
        if type(elem) == list:  # условие: если тип элемента список
            data_list.extend(elem)  # объединение списков
        else:  # альтернативное условие
            l_1.append(elem)  # добавляем элемент в конец списка

    return l_1[::-1]  # возвращаем список в обратном порядке


# 11/2
def task_11(data_list_new: List):  # объявляем функцию с одним параметром (решение через рекурсию)
    l_2 = []  # переменная, которая ссылается на пустой список

    def flattering_1(index_1):  # объявляем функцию с одним параметром
        while index_1 < len(data_list_new_):  # пока индекс меньше длины списка
            if type(data_list_new[index_1]) != list:  # если тип объекла не список
                l_2.append(data_list_new[index_1])  # добавляем объект в новый список
                del data_list_new[index_1]  # удаляем элемент с индексом
                flattering_1(index_1 + 1)  # вызываем функцию (увеличиваем индекс на один)
            else:  # альтернативное условие
                pop_elem = data_list_new.pop(index_1)  # удаляем элемент с индексом
                data_list_new.extend(pop_elem)  # объединение списков

    flattering_1(0)  # вызываем функцию и передаем аргумент 0
    return l_2  # возвращаем новый список


# 1
growth_: float = float(input('Введите рост в м: '))
weight_: float = float(input('Введите вес в кг: '))
index_(growth_, weight_)

# 2
count_side: int = int(input('Введите количество сторон у фигуры (от 3 до 10): '))
print(figures(count_side))

# 3
day_: int = int(input('Введите число: '))
month_: str = input('Введите месяц: ')
year_: int = int(input('Введите год: '))
print(next_day(day_, month_, year_))

# 4
count_products: int = int(input('Введите количество заказанных товаров: '))
print(sum_delivery(count_products))

# 5
numerator_: int = int(input('Ведите числитель: '))
denominator_: int = int(input('Ведите знаменатель: '))
print(fraction(numerator_, denominator_))

# 6
my_list_: List = [1, 3, 4, 2, 6, 7, 0, 4, 'a', 'len', 'flower', 'cat', 10, 19, 32, 'any']
work_with_list(my_list_)

# 7
any_list_ = [1, 2, 3, 4, 3, 2, 5, 7, 8, 0, 4, 6, 8, 31, 3, 5, 7, 8, 19, 12.0, 15.1]
min_num_ = int(input('Введите начало диапазона: '))
max_num_ = int(input('Введите окончание диапазона: '))
cuntRange(any_list_, min_num_, max_num_)

# 8
all_list_ = [1, 2, 3, [1, 2, 3], [4, 3, 1], [10, 19, 17], [21, 10, 5]]
print(count_list_in_list(all_list_))

# 9
first_word_: str = input('Введите первое слово: ')
second_word_: str = input('Введите второе слово: ')
print(anagram(first_word_, second_word_))

# 10
string_ = input('Введите строку: ')
dict_mobile(string_)

# 11
data_list_: List = [1, [2, 3], [4, [15, [6, 7]]], [[[8], 9], 10]]
print(flattering(data_list_))

# 11/2
data_list_new_: List = [1, [2, 3], [4, [15, [6, 7]]], [[[8], 9], 10]]
print(task_11(data_list_new_))