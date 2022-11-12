class CardDeck:

    def __init__(self, card_dict):
        self.dict = card_dict
        self.card_number = -1

    def __next__(self):
        list_of_keys = [key for key in self.dict]
        if self.card_number + 1 < 13:
            self.card_number += 1
            return self.dict[list_of_keys[self.card_number]]


def what_card_suit():
    card_suit = input(
        'Ввeдите карты какой масти вы хотите посчитать (пикиб червыб бубныб трефы) или вы хотите остановиться (стоп)?:')
    if card_suit != 'стоп':
        if card_suit == 'пики':
            object_1 = dict_1
            return object_1
        elif card_suit == 'червы':
            object_2 = dict_2
            return object_2
        elif card_suit == 'бубны':
            object_3 = dict_3
            return object_3
        elif card_suit == 'трефы':
            object_4 = dict_4
            return object_4
    else:
        return False


def busting_cards(object_):
    next_card = input('Хотите посмотреть еще одну карту (да - 1/нет - 2)? ')
    for i in range(13):
        if next_card == '1':
            print(next(object_))
            next_card = input('Хотите посмотреть еще одну карту (1/2)? ')
        else:
            break


def main():
    dict_ = what_card_suit()
    while dict_:
        object_class = CardDeck(dict_)
        busting_cards(object_class)
        print('Вы просмотрели все карты этой масти')
        dict_ = what_card_suit()
    print('Закончен просмотр карт')
    raise StopIteration


dict_1 = {'туз': 'туз пики', 2: '2 пики', 3: '3 пики', 4: '4 пики', 5: '5 пики', 6: '6 пики',
          7: '7 пики', 8: '8 пики', 9: '9 пики', 10: '10 пики', 'валет': 'валет пики',
          'дама': 'дама пики', 'король': 'король пики'}
dict_2 = {'туз': 'туз червы', 2: '2 червы', 3: '3 червы', 4: '4 червы', 5: '5 червы', 6: '6 червы',
          7: '7 червы', 8: '8 червы', 9: '9 червы', 10: '10 червы', 'валет': 'валет червы',
          'дама': 'дамы червы', 'король': 'король червы'}
dict_3 = {'туз': 'туз бубны', 2: '2 бубны', 3: '3 бубны', 4: '4 бубны', 5: '5 бубны', 6: '6 бубны', 7: '7 бубны',
          8: '8 бубны', 9: '9 бубны', 10: '10 бубны', 'валет': 'валет бубны',
          'дама': 'дама бубны', 'король': 'король бубны'}
dict_4 = {'туз': 'туз трефы', 2: '2 трефы', 3: '3 трефы', 4: '4 трефы', 5: '5 трефы', 6: '6 трефы', 7: '7 трефы',
          8: '8 трефы', 9: '9 трефы', 10: '10 трефы', 'валет': 'валет трефы',
          'дама': 'дама трефы', 'король': 'король трефы'}
main()
