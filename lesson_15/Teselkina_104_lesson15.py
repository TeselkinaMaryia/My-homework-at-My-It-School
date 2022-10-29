import json
from typing import Dict, List


# 1
def dict_list(string: str) -> None:  # объявляем функцию с одним параметром
    list_day_product: List = []  # переменная, которая ссылаетяс на пустой список
    while string != 'стоп':  # цикл с условием
        dict_: Dict[str, str] = {}  # переменная которая ссылается на пустой словарь
        list_: List[str] = string.split(' ')  # из строки делвем список
        dict_['название'] = list_[0]  # создаем пары ключ: значение
        dict_['стоимость'] = list_[1]
        list_day_product.append(dict_)  # добавляем словарь в список
        string: str = input('Введите новый товар и его цену: ')
        # переменная, которая ссылается на вводимое с клавиатуры значение

    if string == 'стоп':  # условие
        write_json(list_day_product)  # вызываем функцию


def write_json(list_: List[dict]) -> None:  # объявляем функцию с одним параметром
    with open('DZ_1.json', 'w', encoding='UTF-8') as file:  # открываем файл для записи
        json.dump(list_, file, ensure_ascii=False)  # записываем в файл объект


# 2
def read_json():  # объявляем функцию без параметра
    with open('DZ_1.json', encoding='UTF-8') as file:  # открываем файл для чтения
        py: List[dict] = json.load(file)  # записываем в переменную преобразованный в объект пайтона объект json
        price: int = 0  # переменная, которая ссылается на целое число
        for i in py:  # цикл
            price += int(i['стоимость'])  # добавляем к значению переменной стоимость продукта
        print(f'потрачено денег за день - {price} рублей')  # вывод в кансоль


# 1
string_: str = input('Введите название и стоимость продукта через пробел/стоп: ')
# переменная, которая ссылается на вводимое с клавиатуры значение
dict_list(string_)  # вызываем функцию

# 2
read_json()  # вызываем функцию 
