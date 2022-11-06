class Tomato:
    states = {1: 'появление всходов', 2: 'появление первого листа', 3: 'разрастание наземной части и корней',
              4: 'образование бутонов', 5: 'цветение', 6: 'формирование и созревание плодов'}
    # словарь со стадиями роста

    def __init__(self, index):  # инициализатор, принимает один параметр
        self._index = index
        self._state = 0

    def grow(self):  # метод, продвижение объекта на одну стадию роста
        if self._state < 6:
            self._state += 1
        print(Tomato.states[self._state], ' - ', self._index)

    def is_ripe(self):  # метод, который проверяет, созрел ли объект
        if self._state == 6:
            return True
        else:
            return False


class TomatoBrush:

    def __init__(self, amount):  # инициализатор, принимает один параметр (количество объектов)
        self.tomatoes = [Tomato(index) for index in range(1, amount + 1)]  # создаем список объектов

    def grow_all(self):  # метод, который продвигает на одну стадию роста каждый объект из списка
        for all_objects in self.tomatoes:
            all_objects.grow()

    def all_are_ripe(self):  # метод, который проверяет созрели ли все объекты
        list_ = []
        for object_ in self.tomatoes:
            list_.append(object_.is_ripe())
        if all(list_):
            return True
        else:
            return False

    def give_away_all(self):  # метод, который чистит список объектов
        if self.all_are_ripe():
            self.tomatoes.clear()


class Gardener:

    def __init__(self, name, tomato_bush_obj):  # инициализатор класса, принимает 2 параметра
        self.name = name
        self._plant = tomato_bush_obj

    def work(self):
        # метод, который показывает работу садовника. В течение работы у растения увеличивается рост на одну ступень
        print('Начало дневной работы')
        self._plant.grow_all()
        print('Конец дневной работы')

    def harvest(self):  # метод, который показыкает, можно ли собирать урожай и если можно, то очишает список объектов
        if self._plant.all_are_ripe():
            print('собираем урожай')
            self._plant.give_away_all()
            print('Все убрано. Млжно садить следующий')

        else:
            print('надо подождать')

    @staticmethod
    def knowledge_base():  # статический метод, выводит справку о садоводстве
        print('Справка')


Gardener.knowledge_base()
tomato_bush = TomatoBrush(2)
gardener = Gardener('Tom', tomato_bush)

gardener.work()
gardener.work()
gardener.work()
gardener.work()
gardener.work()
gardener.work()
gardener.harvest()
