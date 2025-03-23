# Задание 1. Видеокарты.

count_video_card = input('Введите количество видеокарт NVIDIA: ')
while type(count_video_card) != int:
    try:
        count_video_card = int(count_video_card)
    except ValueError:
        count_video_card = input('Введите корректное количество видеокарт NVIDIA: ')

key = 1
dict_video_cart = dict()
while key <= count_video_card:
    dict_video_cart['Видеокарта '+ str(key)] = (input(f'Введите модель видеокарты {key} цифрами: '))
    while type(dict_video_cart['Видеокарта ' + str(key)]) != int:
        try:
            dict_video_cart['Видеокарта ' + str(key)] = int(dict_video_cart['Видеокарта ' + str(key)])
        except ValueError:
            dict_video_cart['Видеокарта ' + str(key)] = (input(f'Введите корректную модель видеокарты {key} цифрами (Например : 4070): '))
    key += 1

print('\nКоличество видеокарт: ',count_video_card,)

for key, value in dict_video_cart.items():
    print(key, ': ', value)

dict_video_cart = list(dict_video_cart.values())
set_video_cart = set(dict_video_cart)

print('Старый список видеокарт: ', dict_video_cart)
print('Новый список видеокарт: ', list(set_video_cart))