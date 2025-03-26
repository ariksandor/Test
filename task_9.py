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

'''def alphabetical_display_of_orders(dict_1:dict):
    dict_2 = dict()
    dict_3 = dict()
    list_1 = list()
    summa = 0
    #i = list(dict_1.keys())[0]
    for key, value in dict_1.items():
        #list_1.append(value)
        #for k in
            #for key, value in list_1:
                #dict_3 = value

    print(list_1)'''

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
    return dict_1, '\n\n',  dict_2
number_of_orders = input_correct_number('Введите количество заказов:', 'Введите КОРРЕКТНОЕ количество заказов:') # Количество заказов
#dictionary_of_orders = create_an_order_dictionary(number_of_orders)

#alphabetical_display_of_orders(dictionary_of_orders)
print(create_an_order_dictionary(number_of_orders))
