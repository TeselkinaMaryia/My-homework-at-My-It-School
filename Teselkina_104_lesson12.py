# 4
def function(seconds):
    def days():
        return seconds // (24 * 60 * 60)

    def hours():
        return (seconds - days() * (24 * 60 * 60)) // (60 * 60)

    def minuts():
        return (seconds - days() * (24 * 60 * 60) - hours() * (60 * 60)) // 60

    def seconds_():
        return (seconds - days() * (24 * 60 * 60) - hours() * (60 * 60) - minuts() * 60) % 60

    print(f'{days()} дней, {hours()} часов, {minuts()} минут,{seconds_()} секунд')


seconds_ = int(input('Введите число секунд: '))
function(seconds_)
