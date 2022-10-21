
def keyboard_input():
    try:
        num_1 = int(input('Введите первое число: '))
        num_2 = int(input('Введите второе чило: '))
        division = num_1 / num_2
        print(division)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        keyboard_input()
    except ValueError:
        print('ValueError')
        keyboard_input()
    finally:
        print('We are done!')


keyboard_input()
