import json
from typing import Dict, List


# 1
def write_in_json(string: str) -> None:  # объявляем функцию с одним параметром
    list_day_product = []
    dict_: Dict[str, str] = {}  # переменная, которая ссылается на пустой словарь
    list_: List[str] = string.split(' ')  # переменная, которая ссылается на список из строк
    dict_['название'] = list_[0]  # создаем пару ключ: значение
    dict_['стоимость'] = list_[1]

    list_day_product.append(dict_)
    string_1: str = input('Введите название и стоимость продукта через пробел/стоп: ')
    if string_1 != 'стоп':
        write_in_json(string_1)

    with open('DZ_1.json', 'a', encoding='UTF-8') as file:  # открываем файл
        json.dump(list_day_product, file, ensure_ascii=False)  # записываем объект пайтона в файл


# 1
string_: str = input('Введите название и стоимость продукта через пробел/стоп: ')
# переменная, которая ссылается на вводимое с клавиатуры значение
write_in_json(string_)  # вызываем функцию

