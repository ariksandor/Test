# Задача 8. Товары

goods = {
'Лампа': '12345',
'Стол': '23456',
'Диван': '34567',
'Стул': '45678',
} #dict_1
store = {
'12345': [
{'quantity': 27, 'price': 42},
],
'23456': [
{'quantity': 22, 'price': 510},
{'quantity': 32, 'price': 520},
],
'34567': [
{'quantity': 2, 'price': 1200},
{'quantity': 1, 'price': 1150},
],
'45678': [
{'quantity': 50, 'price': 100},
{'quantity': 12, 'price': 95},
{'quantity': 43, 'price': 97},
],
} #list_1 dict_2
def print_cost_dicts(dict_1, dict_2):
    for key, value in dict_1.items():
        i = 0
        sum_2 = 0
        count = 0
        while i < len(dict_2[value]):
            slovar = dict_2[value][i]
            sum_1 = slovar['quantity'] * slovar['price']
            sum_2 = sum_1 + sum_2
            count = count + slovar['quantity']
            i += 1
        if str(sum_2)[-2:] in ('11', '12', '13', '14'):
            rub = 'рублей'
        elif str(sum_2)[-1] == '1':
            rub = 'рубль'
        elif str(sum_2)[-1] in ('2', '3', '4'):
            rub = 'рубля'
        else:
            rub = 'рублей'

        if str(count)[-2:] in ('11', '12', '13', '14'):
            numb = 'штук'
        elif str(count)[-1] == '1':
            numb = 'штука'
        elif  str(count)[-1] in ('2', '3', '4'):
            numb = 'штуки'
        else:
            numb = 'штук'
        print(f'{key} - {count} {numb}, стоимость {sum_2} {rub}')
print_cost_dicts(goods, store)