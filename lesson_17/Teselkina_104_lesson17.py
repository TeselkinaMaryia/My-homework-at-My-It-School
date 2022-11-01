from typing import List


# DZ
class Method:  # создаем класс

    def __init__(self):  # инициализатор, принимает созданный конструктором объект класса
        self.str_dig: str = input('Введите строку или число: ')
        # объекл класса, который ссылается на вводимую с клавиатуры строку

    def string_digit(self) -> List or int:  # метод класса для работы с объектом класса

        if self.str_dig.isalpha():  # если объект - строка
            list_vowels: List = [x for x in self.str_dig if x in ['a', 'e', 'y', 'u', 'i', 'o']]
            # создаем список через генератор, состоит только из гласных
            list_consonants: List = [x for x in self.str_dig if x not in ['a', 'e', 'y', 'u', 'i', 'o']]
            # список только из согласных, которые есть в нашей строке

            if len(list_vowels) * len(list_consonants) <= self.len_of_something():
                # условие: если произведение количества гласных и согласных <= длинне слова
                return list_vowels
            else:  # альтернативное условие
                return list_consonants

        elif self.str_dig.isdigit():  # альтернативное условие (если строка состоит из чисел)
            list_even: List = [int(x) for x in self.str_dig if int(x) % 2 == 0]
            # создаем список четных чисел через генератор списков
            return sum(list_even) * self.len_of_something()

    def len_of_something(self) -> int:  # метод класса, который возвращает длинну строки
        return len(self.str_dig)


print(Method().string_digit())  # вызываем метод класса 
