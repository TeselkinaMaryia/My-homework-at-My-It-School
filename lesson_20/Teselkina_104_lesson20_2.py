from typing import List


class CardDeck:  # declare the class with name CardDeck
    def __init__(self, list_: List[str]):  # initializer accepts one option (list), return - None
        self.list_: List[str] = list_  # variable - list
        self.value: int = -1  # variable - int

    def __next__(self):  # magic function

        if self.value + 1 < len(self.list_):  # condition
            self.value += 1  # add 1 to the variable value
            return self.list_[self.value]  # built-in function that return the object of the list with definite index
        else:  # alternative condition
            raise StopIteration  # raise Error - StopIteration


list_card: List[str] = ['туз пики', '2 пики', '3 пики', '4 пики', '5 пики', '6 пики', '7 пики', '8 пики', '9 пики',
                        '10 пики', 'валет пики', 'дама пики', 'король пики', 'туз червы', '2 червы', '3 червы',
                        '4 червы', '5 червы', '6 червы', '7 червы', '8 червы', '9 червы', '10 червы', 'валет червы',
                        'дама червы', 'король червы', 'туз бубны', '2 бубны', '3 бубны', '4 бубны', '5 бубны',
                        '6 бубны', '7 бубны', '8 бубны', '9 бубны', '10 бубны', 'валет бубны', 'дама бубны',
                        'король бубны', 'туз трефы', '2 трефы', '3 трефы', '4 трефы', '5 трефы', '6 трефы', '7 трефы',
                        '8 трефы', '9 трефы', '10 трефы', 'валет трефы', 'дама трефы', 'король трефы']
# list variable
one_card: CardDeck = CardDeck(list_card)  # create the object of the class
for i in range(53):  # cycle
    print(next(one_card))  # built-in function that prints a string to the console
