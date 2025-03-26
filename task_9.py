#
from num2words import num2words
def conversion_number_into_numeral(num): # функция перевода числа в числительное
    numeral = num2words(num, to = 'ordinal', lang = 'ru')
    return numeral
def input_correct_number(print_input, print_input_cor): # функция Ввода корректного числа Type -int
    num_1 = input(f'{print_input}\t')
    while type(num_1) != int:
        try:
            num_1 = int(num_1)
        except ValueError:
            num_1 = input(f'{print_input_cor}\t')
    return num_1

def alphabetical_display_of_orders(dict_1:dict, dict_2:dict):
    dict_4 = dict()
    dict_3 = dict()
    #list_1 = list()
    #summa = 0
    copy_dict_1 = dict_1.copy()
    for key, value in dict_1.items():
        sum_1 = 0
        for key_1, value_1 in copy_dict_1.items():

            if value == value_1:
                #dict_4[key] = ''
                if dict_2[key][0]['пицца'] == dict_2[key_1][0]['пицца']:

                    sum_1 = sum_1 + dict_2[key_1][0]['количество']
                    dict_3[dict_2[key_1][0]['пицца']] = sum_1
                else:
                    dict_3.update({dict_2[key_1][0]['пицца']: dict_2[key_1][0]['количество']})
                copy_dict_1[key_1] = ''
                #dict_4[key] = dict_3
            #pizza = dict_2[key][0]['пицца']
            #count_1 = dict_2[key][0]['количество']

    print(dict_4)


def create_an_order_dictionary(num): # Функция создания словаря с заказами
    i = 1
    dict_1 = dict()
    dict_2 = dict()
    while i <= num:
        dict_3 = {}
        list_1 = []
        numeral = str(conversion_number_into_numeral(i))
        print(f'{numeral[0].upper()}{numeral[1:len(numeral) + 1]} заказ: ')
        buyer = input('Фамилия покупателя:\t')  # покупатель
        pizza = input('Введите название пиццы:\t')
        amount_of_pizza = input_correct_number('Введите количество выбранной пиццы:','Введите КОРРЕКТНОЕ количество заказов:')  # Количество пиццы
        dict_3['пицца'] = pizza
        dict_3['количество'] = amount_of_pizza
        list_1.append(dict_3)
        dict_2.update({i : list_1})
        dict_1[i] = buyer
        i += 1
    return dict_1, dict_2
number_of_orders = input_correct_number('Введите количество заказов:', 'Введите КОРРЕКТНОЕ количество заказов:') # Количество заказов

dictionary_of_orders_1, dictionary_of_orders_2 = create_an_order_dictionary(number_of_orders)
alphabetical_display_of_orders(dictionary_of_orders_1, dictionary_of_orders_2)


