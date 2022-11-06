import string


class Alphabet:

    def __init__(self, lang, str_letters):
        self.lang = lang
        self.letters = list(str_letters)

    def print_(self):
        print('алфавит -', self.letters)

    def letters_num(self):
        return f'количество букв в алфавите - {len(self.letters)}'


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_an_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        else:
            return False

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print('Some english text')


en_alphabet_ex = EngAlphabet()
en_alphabet_ex.print_()
print(en_alphabet_ex.letters_num())
print(en_alphabet_ex.is_an_letter('F'))
print(en_alphabet_ex.is_an_letter('Щ'))
EngAlphabet.example()