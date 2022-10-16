from typing import List, Dict


# 1
def index_(growth: float, weight: float):
    index: float = weight / growth ** 2
    if index < 16.5:
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
def figures(integer: int) -> str:
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
def next_day(day: int, month: str, year: int) -> tuple:
    leap_year: List[int] = [i for i in range(1904, 3000, 4)]
    if year in leap_year:
        day_in_month: Dict[str:int] = {'январь': 31, 'февраль': 29, 'март': 31, 'апрель': 30, 'май': 31, 'июнь': 30,
                                       'июль': 31, 'август': 31, 'сентябрь': 30, 'октябрь': 31,
                                       'ноябрь': 30, 'декабрь': 31}
    else:
        day_in_month: Dict[str:int] = {'январь': 31, 'февраль': 28, 'март': 31, 'апрель': 30, 'май': 31, 'июнь': 30,
                                       'июль': 31,
                                       'август': 31, 'сентябрь': 30, 'октябрь': 31, 'ноябрь': 30, 'декабрь': 31}
    if day < day_in_month[month]:
        return day + 1, month, year
    elif day == day_in_month[month] and month != 'декабрь':
        list_month: List[str] = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
                                 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
        return 1, list_month[list_month.index(month) + 1], year
    elif day == day_in_month[month] and month == 'декабрь':
        return 1, 'январь', year + 1


# 4
def sum_delivery(product: int) -> float:
    if product == 1:
        return 10.95
    else:
        return 10.95 + 2.95 * (product - 1)


# 5
def fraction(numerator: int, denomenator: int):
    list_num_denomenator = [_ for _ in range(1, denomenator + 1)]
    multiplicity_for_numerator = []
    for number in list_num_denomenator:
        if numerator % number == 0 and denomenator % number == 0:
            multiplicity_for_numerator.append(number)
    return numerator / multiplicity_for_numerator[-1], denomenator / multiplicity_for_numerator[-1]


# 6
def work_with_list(my_list: List):
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
def cuntRange(any_list, min_num, max_num):
    for object_ in any_list:
        if type(object_) == int:
            interval_int = [i for i in range(min_num, max_num + 1)]
            if object_ in interval_int:
                print(f'{object_} - {any_list.count(object_)}', end=' ')
        elif type(object_) == float:
            interval_float = [float(i) for i in range(min_num, max_num + 1)]
            if min(interval_float) < object_ < max(interval_float):
                print(f'{object_} - {any_list.count(object_)}', end=', ')


# 8
def count_list_in_list(all_list: List) -> int:
    count_lists: int = 0
    for _ in all_list:
        if type(_) == list:
            count_lists += 1
    return count_lists


# 9
def anagram(first_word: str, second_word: str):
    if second_word == first_word[::-1]:
        return 'Слова являются анаграммами'
    else:
        return 'Слова не являются анаграммами'


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