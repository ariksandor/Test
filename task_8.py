# from statistics import quantiles

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
    #slovar = dict()
    sum_1 = 0
    sum_2 = 0
    for key, value in dict_1.items():
        i = 0
        while i < len(dict_2[value]):
            slovar = dict_2[value][i]
            sum_1 = slovar['quantity'] * slovar['price']
            sum_2 = sum_1 + (slovar['quantity'] * slovar['price'])
            i += 1
        print(sum_2)
        #print(f'{key} - {dict_2[value][0]}')
    #print(sum_1)
print_cost_dicts(goods, store)