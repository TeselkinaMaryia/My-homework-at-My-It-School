from typing import Any


# 1
def decorator_1(func: Any) -> Any:  # decorator, accepts function and return body of the func wrapper

    def wrapper(*args: Any, **kwargs: Any) -> int:  # func wrapper. Accepts positional and keyword options
        wrapper.count += 1  # increase by one variable value
        result: int = func(*args, **kwargs)  # variable. takes the result of function work
        print(f'we call {func.__name__}, {wrapper.count} times')  # built-in func that output a string to the console
        return result  # return the  variable value

    wrapper.count = 0  # variable
    return wrapper  # return the body of the function


@decorator_1  # decorating the function
def sum_(a: int, b: int):  # function accepts two options
    return a + b  # return the sum of the two digits


sum_(1, 3)  # call the function and transfer two positional arguments
sum_(4, 5)  # call the function and transfer two positional arguments
sum_(b=3, a=6)  # call the function and transfer two keyword arguments
