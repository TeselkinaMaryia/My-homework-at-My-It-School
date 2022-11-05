# 1
class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price - (self._price * discount * 0.01)
        return final_price


class SmallHouse(House):

    def __init__(self, price):
        super().__init__(40, price)
        self.square = 40


class Human:
    default_name = 'Maryia'
    default_age = 22

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        return f'Name - {self.name},age - {self.age}, house - {self.__house}, cash - {self.__money}'

    @staticmethod
    def default_info():
        return f'default name - {Human.default_name}, default age - {Human.default_age}'

    def earn_money(self, income):
        self.__money += income

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
            return 'Дом куплен'
        else:
            return f'Пополните ваш баланс. У вас не хватает на покуптку дома'

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house


human_1 = Human()
human_1.earn_money(200)

small_house_1 = SmallHouse(9500)
human_1.earn_money(10000)
print(human_1.buy_house(small_house_1, 10))
print(human_1.info())
