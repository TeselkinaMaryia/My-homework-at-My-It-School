import numpy as np

"""
Импорт модуля numpy: 
- import numpy
- import numpy as np
np — это общепринятое название, которое стало правилом и упростило процесс написания кода, 
поэтому, один раз прописав import numpy as np, в последующих строках можно использовать np вместо numpy
- from numpy import *
Также можно импортировать numpy прямо в используемое пространство имен, 
чтобы вообще не использовать функции через точку, а вызывать их напрямую
"""

# Создание массивов
array_1 = np.array([1, 2, 3], int)
array_2 = np.array([1, 2, 3, 4, 5, 6], float)
# функция array принимает два аргумента: список для конвертации в массив и тип для каждого элемента.
print(type(array_1), array_1, array_2, sep='\n')

# Создание срезов и вызов элемента массива по индексу
array_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], int)
print(
    array_1[1],
    array_1[:5],
    array_1[::-1], sep='\n'
)

# Многомерные массивы
array_1 = np.array([[1, 2, 3], [4, 5, 6]], int)

print(array_1[0, 0],  # можно указывать через ,
      array_1[1, 2],
      array_1[0, :],  # Используйте ":" в измерении для указывания использования всех элементов этого измерения
      array_1[1, :],  # выводит в кансоль весь массив под индексом 1 - [4, 5, 6]
      array_1[-1, -2], sep='\n')  # выводит предпоследний символ последнего измерения

# Итерирование массивов
a = np.array([[1, 2, 3],
              [4, 5, 6]])
for _ in a:
    print(_)

a = np.array([[1, 2, 3],
              [4, 5, 6]])

for _ in a.flat:
    print(_)

# Наиболее важные атрибуты объектов ndarray
array_1 = np.array([[1, 2, 3],
                    [4, 5, 6]], int)
print(array_1.ndim,  # число измерений (осей) массива
      array_1.shape,  # размер массива, его форма. 1- число строкб 2- число столбцов
      array_1.size,  # количество элементов массива
      array_1.dtype,  # описывает тип элементов массива
      array_1.itemsize,  # размер каждого элемента массива в байтах
      sep='\n')

"""
Функции: 
array() трансформирует вложенные последовательности в многомерные массивы
zeros() создает массив из нулей
ones() — массив из единиц
eye() создаёт единичную матрицу (двумерный массив)
empty() создает массив без его заполнения
arange(), аналогичная встроенной в Python range()
linspace(), создает последовательности чисел (вместо шага в качестве одного из аргументов принимает число, 
равное количеству нужных элементов)
fromfunction(): применяет функцию ко всем комбинациям индексов
"""
new_array = np.zeros((3, 5))
print(new_array)

new_array = np.ones((2, 1, 3))
print(new_array)

new_array = np.eye(4)
print(new_array)

new_array = np.empty((2, 3))
print(new_array)

new_array = np.arange(10, 30, 5)
print(new_array)

new_array = np.arange(0, 2, 0.5)
print(new_array)

new_array = np.linspace(0, 2, 9)  # 9 чисел от 0 до 2 включительно
print(new_array)


def f1(num_1, num_2):
    return 3 + num_1 + num_2


print(np.fromfunction(f1, (3, 3)))

# Печать массивов
# 1
print(np.arange(0, 5000, 2))  # автоматически скрывается средняя часть
# 2
array_ = np.arange(0, 2000, 1)
np.set_printoptions(threshold=5000)
print(array_)
# В параметре threshold можно задать величину массива (количество элементов в нем)
# при превышении которого массив выводится в сокращенной записи

# Базовые операции
# +
array_1 = np.array([20, 30, 40, 50])
array_2 = np.arange(4)  # [0, 1, 2, 3]
print(array_1 + array_2)
# -
array_1 = np.array([20, 30, 40, 50])
array_2 = np.arange(4)  # [0, 1, 2, 3]
print(array_1 - array_2)
# *
array_1 = np.array([20, 30, 40, 50])
array_2 = np.arange(4)  # [0, 1, 2, 3]
print(array_1 * array_2)
# /
array_1 = np.array([20, 30, 40, 50])
array_2 = np.arange(4)  # [0, 1, 2, 3]
print(array_1 / array_2)  # При делении на 0 указывается ошибка (возвращается inf (бесконечность))
# **
array_1 = np.array([20, 30, 40, 50])
array_2 = np.arange(4)  # [0, 1, 2, 3]
print(array_1 ** array_2)
# %
array_1 = np.array([20, 30, 40, 50])
array_2 = np.arange(1, 5)  # [1, 2, 3, 4]
print(array_1 % array_2)
# //
array_1 = np.array([20, 30, 40, 50])
array_2 = np.arange(1, 5)  # [1, 2, 3, 4]
print(array_1 // array_2)

# Также можно производить математические операции между массивом и числом.
# В этом случае к каждому элементу прибавляется это число.
array_1 = np.array([20, 30, 40, 50])
print(array_1 + 1,
      array_1 * 3,
      array_1 ** 2,
      array_1 > 30, sep='\n')

# NumPy также предоставляет множество математических операций для обработки массивов:
array_1 = np.array([1, 10, 20, 30, 40])
print(np.cos(array_1),
      np.arctan(array_1),
      np.degrees(array_1),
      sep='\n')
# нахождение индексов минимального и максимального числа
a = np.array([1, 2, 3, 4, 5, 6, 7, 8], int)
print(a.argmin(), a.argmax())

"""
Для многомерных массивов каждая из функций может принять дополнительный аргумент axis и в зависимости от его значения 
выполнять функции по определенной оси, помещая результаты исполнения в массив:

"""
a = np.array([[0, 2],
              [3, -1],
              [3, 5]], int)

print(np.min(a, axis=0),
      np.min(a, axis=1),
      np.max(a, axis=0),
      np.max(a, axis=1),
      sep='\n')

# округление
a = np.array([1.1, 1.5, 1.9], float)  # возвращают нижние (округлённое) значение
print(np.floor(a),  # возвращают верхние (округлённое) значение
      np.ceil(a),  # возвращают ближайшие (округлённое) значение
      np.rint(a), sep='\n')
# Сортировка
a = np.array([6, 2, 5, -1, 0, 876], int)
a.sort()
print(a)

# Булевое сравнение
a = np.array([6, 2, 5, -1, 0], int)
b = np.array([2, 4, 5, 8, 1], int)
print(a > b,
      a == b,
      a < b, sep='\n')

# Методы
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], int)

print((1 in a),  # используется для проверки на наличие элемента в массиве
      a.reshape((2, 5)),  # переформирование массива
      a.copy(),  # создания копии существующего массива
      a.transpose(),  # Транспонирование массивов
      sep='\n')

a = np.array([[1, 2, 3], [4, 5, 6]], int)
print(a.flatten())  # переконвертация многомерного массива в одномерный

# Объединение массивов
#
a = np.array([[1, 2], [3, 4]], int)
b = np.array([[5, 6], [7, 8]], int)
print(np.concatenate((a, b), axis=0),
      'Другой вариант',
      np.concatenate((a, b), axis=1), sep='\n')
#
a = np.array([[1, 2], [3, 4]], int)
b = np.array([[5, 6], [7, 8]], int)
print(np.vstack((a, b)),
      np.hstack((a, b)), sep='\n')

a = np.array([1, 2, 3, 4], int)
b = np.array([5, 6, 7, 8], int)
print(np.column_stack((a, b)))

# Разбиение массивов
a = np.arange(12)
print(a,
      a.reshape((2, 6)),
      np.hsplit(a, 3),  # Разбить на 3 части
      np.hsplit(a, (2, 4)), sep='\n')  # Разрезать a после 2 и 4 столбца

# Копии и представления
a = np.arange(12)
b = a
print(b is a)

# поверхностная копия
# Метод view() создает новый объект массива, являющийся представлением тех же данных.
a = np.arange(12)
b = a.view()
print(b is a)

# Глубокая копия
b = a.copy()

# Работа с формой
array_ = np.array([[[0, 1, 2],
                    [10, 12, 13]],

                   [[100, 101, 102],
                    [110, 112, 113]]])
print(array_.shape)
# Изменение формы
array_.ravel()  # Делает массив плоским
array_.transpose()  # Транспонирование
array_.reshape((3, 4))  # Изменение формы
array_.shape = (6, 2)  # Изменение формы
