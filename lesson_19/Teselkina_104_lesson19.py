from typing import Any, List
import logging


# 1 classwork
def decorator_1(func: Any) -> Any:  # decorator, accepts function and return body of the func wrapper

    def wrapper(*args: Any, **kwargs: Any) -> int:  # func wrapper. Accepts positional and keyword options
        wrapper.count += 1  # increase by one variable value
        result: int = func(*args, **kwargs)  # variable. takes the result of function work
        print(f'we call {func.__name__}, {wrapper.count} times')  # built-in func that output a string to the console
        return result  # return the  variable value

    wrapper.count = 0  # variable
    return wrapper  # return the body of the function


@decorator_1  # decorating the function
def sum_(a: int, b: int) -> int:  # function accepts two options
    return a + b  # return the sum of the two digits


# 2 homework
def decorator_2(func):  # decorator accepts function

    def wrapper(list_):  # function accepts the list
        res, old_list = func(list_)[-1], func(list_)[0]  # two variables from func

        for dig in res:  # cycle
            old_list.remove(dig)  # delete an element from list (list of nums that divider by three)
        print(f'nums that do not divider by three - {old_list}')  # output the string to the console
        return res  # return the variable

    return wrapper  # return the body of the function wrapper


@decorator_2  # decorating the function
def multiples(list_: list) -> tuple:  # function accept list and return tuple
    new_list = []  # variable that refers to an empty list
    for i in list_:  # cycle
        if type(i) == list:  # condition: if the type of list object = list
            new_list.extend(i)  # add to a new list element by element of object
        else:  # alternative condition
            new_list.append(i)  # add an element to the end of the list

    multiples_of_three = [num for num in new_list if num % 3 == 0]  # list generator, add nums  divisible by three
    return new_list, multiples_of_three  # return tuple


# 3
def debug(func: Any) -> Any:  # decorator accepts the function

    def wrapper(*args: Any) -> Any:  # function accepts many positional options
        print('Start work')  # outputting the information to the console
        res = func(*args)  # variable refers to the function work result
        if res is not None:  # condition
            print(f'Function - {func.__name__} - with arguments {args}. Result - {res}')
            # built-in function output string to the console
            return res  # return variable value

    return wrapper  # return the body of the function


@debug  # decoration the function
def division(num_1: int, num_2: int) -> float or None:  # function accepts two positional options
    try:  # block of the code where exceptions can be thrown
        end_difference = num_1 / num_2
        return end_difference  # return variable value
    except Exception:  # block of code that handles exceptions
        logging.exception('Exception occurred')  # output to the console string and the information of exception
        print()

        num_1_ = int(input('enter new divident: '))
        num_2_ = int(input('enter new divider: '))
        division(num_1_, num_2_)  # call the function and transfer two positional arguments


# 1 classwork
sum_(1, 3)  # call the function and transfer two positional arguments
sum_(4, 5)  # call the function and transfer two positional arguments
sum_(b=3, a=6)  # call the function and transfer two keyword arguments


# 2
list_1: List[Any] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # variable, type = list
print(multiples(list_1))  # built-in function, output the result of function work to console


# 3
num_1: int = int(input('enter the divident: '))  # variable refers to the number entered from the keyboard
num_2: int = int(input('enter the divider: '))
division(num_1, num_2)  # call the function and transfer two positional arguments
