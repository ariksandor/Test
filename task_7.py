films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
ad_count_films = input('Введите сколько фильмов хотите добавить: ')
while type(ad_count_films) != int:
    try:
        ad_count_films = int(ad_count_films)
    except ValueError:
        ad_count_films = input('Введите (корректное количество) сколько фильмов хотите добавить: ')

i = 0
list_lowe_films = list()
lowe_film = ''
while i < ad_count_films:
    lowe_film = input('Введите название фильма: ')
    for film in films:
        if lowe_film == film:
            list_lowe_films.append(lowe_film)

    #lowe_film = input(f'Ошибка: фильма {lowe_film} нет :(\nВведите название фильма: ')
    i += 1

print(list_lowe_films)