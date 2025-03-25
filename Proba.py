

from num2words import num2words

print(num2words(42, to = 'ordinal', lang = 'ru'))  # Выведет forty-two
print(num2words(42, to = 'ordinal')) # Выведет forty-second
print(num2words(42, lang = 'fr'))  # Выведет quarante-deux

def conversion_number_into_numeral(num):
    numeral = num2words(num, to = 'ordinal', lang = 'ru')
    return numeral




dict_1 = {
    1 : {'Иванов' : {'pizza' : 'Мексиканская',
                     'count' : 22}},
    2 : {'Петров' : {'pizza' : 'Деревенская',
                     'count' : 22}}
}
print(dict_1)

def input_correct_number(print_input, print_input_cor):
    num_1 = input(f'{print_input}\t')
    while type(num_1) != int:
        try:
            num_1 = int(num_1)
        except ValueError:
            num_1 = input(f'{print_input_cor}\t')
    return num_1

print('a', end='')
print('b', end='')
print('c')