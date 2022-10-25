import numpy as np
from typing import List


# 1
def sum_() -> tuple:  # объявляем функцию без параметра, которая возвращает кортеж
    with open('sting_nums.txt') as file:
        # открываем файл в режиме чтения (по умолчанию) и записываем его в переменную по новым именем
        sum_int: int = 0  # переменная, которая ссылается на число
        my_string: str = ''  # переменная, которая ссылается на строку
        for elem in file.readline().replace('_', ' ').split(' '):
            # цикл: для каждого элемента в первой строке текстового документа,
            # где все элементы разделены в местах пробела и представлены в виде списка
            if elem.isdigit():  # условие: если элемент - чило
                sum_int += int(elem)
                # приводим элемент к типу данных целые числа и добавляем его значение к значению переменной
            elif elem.isalpha():  # альтернативное условие: если элемент состоит из букв
                my_string += elem + ' '  # добавляем элемент и пробел после него к строке
        return sum_int, my_string  # возвращаем кортеж из значения суммы всех чисел и строки


# 2
def sort_list() -> list:  # объявляем функцию без параметра, которая будет возвращать отсортированный список
    with open('str_int_lines.txt') as file:  # открываем текстовый файл для чтения и обозначаем его как file
        list_int: List = []  # переменная, которая ссылается на пустой список
        list_str: List = []
        for elem in file.read().split('\n'):  # для каждого элемента из списка
            if elem.isdigit():  # условие: если элемент - число
                list_int.append(int(elem))  # добавляем в конец списка
            else:  # альтернативное условие
                list_str.append(elem)  # добавляем элемент в конец другого списка
        list_int.sort()  # сортируем список из чисел
        list_str.sort(key=len)  # сортируем список из строк по длине строки
        list_int.extend(list_str)  # объединяем списки
        return list_int  # возвращаем список


# 3
def write_text(string: str) -> str:  # объявляем функцию с одним параметром, которая возвращает строку
    file = open('write_lines.txt', 'a', encoding='utf-8')  # открываем файл для добавления текста
    try:  # действие, которое может повлечь исключение
        file.write(string + '\n')  # запись в файл строки с новой строчки
    except Exception:  # если было вызвано любое исключение
        return 'some Error'  # возвращаем строку
    finally:  # блок инструкции, который выполняется всегда
        file.close()  # закрываем текстовый файл


# 4
def count_lines():  # объявляем функцию без параметра
    with open('count.txt', encoding='utf-8') as file:  # открываем файл в режиме чтения и обозначаем его как file
        lines: int = 0  # переменная, которая ссылается на число
        for elem in file.read().split('\n'):  # для каждого элемента в списке из строк
            print(f' В строке: {elem} -  {len(elem)} символов')  # вывод в кансоль элемента и его длины
            lines += 1  # добавляем 1 к значению переменной
        print(f'количество строк - {lines}')  # выводим в кансоль значение количества строк в файле


# DZ
def sort_array(arr: List) -> None:  # объявляем функцию с одним параметром
    file = open('write_sort_array.txt', 'a', encoding='utf-8')  # открываем файл в режиме добавления текста
    try:  # блок когда, где могут возникнуть исключения
        arr_int_str: List = sorted(arr, key=lambda x: type(x) == str)
        # сортируем список, чтобы в начале были числа, а в конце строки
        for index_ in range(0, len(arr_int_str) - 1):  # цикл по индексам списка
            if type(arr_int_str[index_]) == str and type(arr_int_str[index_ - 1]) == int:
                # если тип объекта с данным индексом - строка, а тип предыдущего объекта - целое число
                arr_str: List = sorted(arr_int_str[index_:], key=len)  # сортируем срез списка из строк
                arr_int: List = sorted(arr_int_str[: index_])  # сортируем срез списка из чисел
                for i in arr_str + arr_int:  # для каждого элемента объединенного списка
                    file.write(str(i) + '\n')  # записываем преобразованый в строку объект на новую строку

    finally:  # блок кода обязательный для выполнения
        file.close()  # закрываем файл


# extra 1
def write_in_file(add_string: str) -> None:  # объявляем функцию с одним параметром
    with open('extra_1.txt', 'w', encoding='utf-8') as file:  # открываем файл для записи
        elements = sorted(add_string.split(' '), key=lambda x: x.isalpha())
        # получаем из строки список и сортируем его, чтобы в начале были числа, а в конце строки
        for elem in elements:  # для каждого элемента списка
            if elem.isdigit():  # условие: если элемент - число
                file.write(elem + ' ')  # записываем элемент через пробел
            elif elem.isalpha() and elements[elements.index(elem) - 1].isdigit():
                # если элемент состоит из букв, а прошлый из чисел
                file.write('\n')  # переносим каретку на следующую строку и добавляем элемент
                file.write(elem + ' ')
            elif elem != elements[-1]:  # если элемент не последний в списке
                file.write(elem + ' ')  # добавляем элементы через пробел
            else:
                file.write(elem)


def read_file():  # объявляем функцию без параметра
    file = open('extra_1.txt', encoding='utf-8')  # открываем файл в режиме чтения
    try:  # блок кода, где могут возникать исключения
        text_list = file.read().replace(' \n', ' ').split(' ')
        # посимвольное чтение текстового документа, делаем из строки список
        for elem in text_list:  # цикл: для каждого элемента списка
            if elem.isdigit() and text_list[text_list.index(elem) + 1].isalpha():
                # ищем индекс элемента, до которого до которого будут числа, а после которого строки
                index_ = text_list.index(elem) + 1

                new_list_int: List[int] = [int(num) for num in text_list[:index_]]  # список из чисел
                new_list_int.sort()  # сортируем по возрастанию
                new_list_str: List = sorted(text_list[index_:], key=len)
                # сортируем срез, сотоящий только из строк по длине
                total = new_list_int + new_list_str  # объединяем списки

                print(*total)  # выводим распакованный список
    finally:  # блок кода, который выполняется всегда
        file.close()  # закрываем файл


def main():  # объявляем функцию
    add_string_ = input('Введите строку: ')  # переменная, которая ссылается на вводимую с клавиатуры строку
    write_in_file(add_string_)  # вызываем функцию и передаем ей аргумент

    read_file()  # вызываем следующую функцию


# extra 2
def magic_square(string: str, number: int) -> bool:  # объявляем функцию с двумя параметрами
    list_: List = []  # переменная, которая ссылается на пустой список
    for i in string.split(' '):  # для каждого элемента с списке из разделенной строки
        list_.append(int(i))  # добавляем в конец списка элемент приведенный к типу данных - целое число

    array = np.array(list_)  # переменная, которая ссылается на массив
    end_array = array.reshape(number, number)  # создаем новый многомерный массив из одномерного (изменяя форму)
    list_sum: List = []  # переменная, которая ссылается на пустой список

    for i in range(0, number - 1):
        list_sum.append(sum(end_array[i, :]))  # добавляем в конец списка сумму элементов строки
        list_sum.append(sum(end_array[:, i]))  # добавляем в конец списка сумму элементов столбца

    list_sum.append(sum(end_array.diagonal(axis1=0, axis2=1)))  # добавляем в конец списка сумму элементов диагонали
    list_sum.append(sum(end_array.diagonal(axis1=1, axis2=0)))

    if int(sum(list_sum) / len(list_sum)) == list_sum[0]:  # есои все элементы списка равны
        return True
    else:
        return False


# 1
# print(sum_())  # вызываем функцию

# 2
# print(sort_list())  # вызываем функцию

# 3
# string_: str = input('Введите строку: ')  # переменная, которая ссылаетяс на вводимую пользователем строку
# while string_ != '':  # пока переменная не является пустой строкой
#     write_text(string_)  # вызываем функцию
#     string_: str = input('Введите новую строку: ')

# 4
# count_lines()  # вызываем функцию

# DZ
# arr_: List = [1, 2, 3, 4, 'len', 'sort', 'eat', 45, 678, 'breakfast', 31, 842, 'doll', 'cat', 5]
# # переменная, которая ссылается на список объектов
# sort_array(arr_)  # вызываем функцию

# extra 1
# main()

# extra 2
# number_: int = int(input('Введите одно число (количество столбцов и строк в матрице): '))
# string_: str = input(f'Введите {number_ ** 2} чисел через пробел: ')
# print(magic_square(string_, number_))
