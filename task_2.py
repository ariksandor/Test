# Задача 2. Часы

def watch_the_clock(min):
    res = int(min / 60)
    res_1 = min - res * 60
    print('\nКоличество полных часов в минутах:\t', res)
    print('\nОсталось минут:\t' , res_1)

n = input('Введи количество минут:\t')
while type(n) != int:
    try:
      n = int(n)
    except ValueError:
      n = input('Введи количество минут в виде целого числа:\t')

watch_the_clock(n)