from typing import List, Dict


# 1
def factorial(num: int) -> int:
    if num != 1:
        return num * factorial(num - 1)
    else:
        return num * 1


# 2
def fibonacci(n: int):
    sequence: List[int] = [0, 1]
    for i in range(20):
        new_num: int = sequence[-1] + sequence[-2]
        sequence.append(new_num)
        try:
            if n in sequence:
                print(*sequence[:sequence.index(n) + 1])
        except Exception as e:
            print(e)


# 3
def new_dict(dict_1_: Dict, dict_2_: Dict) -> Dict:
    dict_1_.update(dict_2_)
    keys = dict_1_.keys()
    new: List = sorted(keys, key=len)
    dict_3: Dict = {new[i]: dict_1_[new[i]] for i in range(len(new))}
    return dict_3


# task 2
def work_with_string(our_str):
    without = ''
    different = ''
    for symbol in our_str:
        if symbol not in ['.', ',', '?', '"', "'", '!']:
            without += symbol
            different += symbol
        else:
            different += ' '
    return without, different


def lower_string(our_str):
    lower_str = ''
    for symbol in our_str:
        if symbol != symbol.upper():
            lower_str += symbol
        elif symbol == ' ':
            lower_str += ' '
    return lower_str


def upper_string(our_str):
    new_str = our_str.upper()
    return new_str


def vice_versa(our_str):
    new_str = our_str.swapcase()
    return new_str


# 1
# number = int(input('Your number: '))
# print(f"factorial {number} = {factorial(number)}")

# 2
# number_ = int(input('Number = '))
# fibonacci(number_)

# 3
# dict_1 = {'верный': [11, 55.2, 'слон'], 'фиолетовый': 15, 'орда': 'восемь'}
# dict_2 = {'ода': {52, 99, 2}, 'сороконожка': {110, 'слово', 15}}
# print(new_dict(dict_1, dict_2))

# task 2
# string = 'Что это было?. ...Я не ожидал увидеть подобного, но мне придется принять решение'
# print(work_with_string(string), lower_string(string), upper_string(string), vice_versa(string), sep='\n')
