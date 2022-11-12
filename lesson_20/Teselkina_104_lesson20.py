from typing import Dict, List, Any


class CardDeck:  # declare a class

    def __init__(self, card_dict: Dict):  # initializer accepts dict as an option
        self.dict: Dict[Any, str] = card_dict  # variable
        self.card_number: int = -1  # variable

    def __next__(self) -> str:  # magic function which returns string
        list_of_keys: List[Any] = [key for key in self.dict]  # list variable
        if self.card_number + 1 < 13:  # condition
            self.card_number += 1
            return self.dict[list_of_keys[self.card_number]]  # built-in function which returns string


def what_card_suit() -> Dict or None:  # create a function
    card_suit: str = input(
        'Ввeдите карты какой масти вы хотите посчитать (пикиб червыб бубныб трефы) или вы хотите остановиться (стоп)?:')
    # string variable
    if card_suit != 'стоп':  # condition
        if card_suit == 'пики':
            return dict_1
        elif card_suit == 'червы':
            return dict_2
        elif card_suit == 'бубны':
            return dict_3
        elif card_suit == 'трефы':
            return dict_4
    else:  # alternative condition
        return False


def busting_cards(object_):  # create a function that accepts one option and return None
    next_card: str = input('Хотите посмотреть еще одну карту (да - 1/нет - 2)? ')  # string variable
    for i in range(13):  # cycle for
        if next_card == '1':  # condition
            print(next(object_))  # built-in function that prints the variable tj the console
            next_card: str = input('Хотите посмотреть еще одну карту (1/2)? ')
        else:  # alternative condition
            break  # function terminates the cycle prematurely


def main():  # create the function without options
    dict_ = what_card_suit()  # call the function and assign the result of her work to a variable
    while dict_:  # cycle
        object_class: CardDeck = CardDeck(dict_)  # create an object of CardDeck class
        busting_cards(object_class)  # call the function and transfer the argument
        print('Вы просмотрели все карты этой масти')  # print to the console
        dict_ = what_card_suit()  # call the function
    print('Закончен просмотр карт')
    raise StopIteration  # raise an Error


dict_1: Dict[Any, str] = {'туз': 'туз пики', 2: '2 пики', 3: '3 пики', 4: '4 пики', 5: '5 пики', 6: '6 пики',
                          7: '7 пики', 8: '8 пики', 9: '9 пики', 10: '10 пики', 'валет': 'валет пики',
                          'дама': 'дама пики', 'король': 'король пики'}
dict_2: Dict[Any, str] = {'туз': 'туз червы', 2: '2 червы', 3: '3 червы', 4: '4 червы', 5: '5 червы', 6: '6 червы',
                          7: '7 червы', 8: '8 червы', 9: '9 червы', 10: '10 червы', 'валет': 'валет червы',
                          'дама': 'дамы червы', 'король': 'король червы'}
dict_3: Dict[Any, str] = {'туз': 'туз бубны', 2: '2 бубны', 3: '3 бубны', 4: '4 бубны', 5: '5 бубны', 6: '6 бубны',
                          7: '7 бубны', 8: '8 бубны', 9: '9 бубны', 10: '10 бубны', 'валет': 'валет бубны',
                          'дама': 'дама бубны', 'король': 'король бубны'}
dict_4: Dict[Any, str] = {'туз': 'туз трефы', 2: '2 трефы', 3: '3 трефы', 4: '4 трефы', 5: '5 трефы', 6: '6 трефы',
                          7: '7 трефы', 8: '8 трефы', 9: '9 трефы', 10: '10 трефы', 'валет': 'валет трефы',
                          'дама': 'дама трефы', 'король': 'король трефы'}
# dict variables
main()  # call main function
