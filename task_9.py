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
number_of_orders = input_correct_number('Введите количество заказов:', 'Введите КОРРЕКТНОЕ количество заказов:') # Количество заказов

#dictionary_of_orders = dict() # Словарь заказов

#buyer = input('Введите Фамилию покупателя:\t') # покупатель

#pizza = input('Введите название пиццы:\t') # Название пиццы

#amount_of_pizza = input_correct_number('Введите количество выбранной пиццы:', 'Введите КОРРЕКТНОЕ количество заказов:') # Количество пиццы

def create_an_order_dictionary(num): # Функция создания словаря с заказами
    i = 1
    dict_1 = dict()
    dict_2 = dict()
    dict_3 = dict()
    while i <= num:
        dict_3.clear()
        dict_2.clear()
        numeral_1 = str(conversion_number_into_numeral(i))
        print(f'{numeral_1[0].upper()}{numeral_1[1:len(numeral_1)+1]} заказ: ')
        buyer = input('Фамилия покупателя:\t')  # покупатель
        pizza = input('Введите название пиццы:\t')
        amount_of_pizza = input_correct_number('Введите количество выбранной пиццы:','Введите КОРРЕКТНОЕ количество заказов:')  # Количество пиццы
        dict_3['пицца'] = pizza
        dict_3['количество'] = amount_of_pizza
        dict_2[buyer] = dict_3
        dict_1[i] = dict_2
        i += 1
    return dict_1
dictionary_of_orders = create_an_order_dictionary(number_of_orders)
