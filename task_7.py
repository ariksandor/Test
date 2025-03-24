films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
ad_count_films = input('Введите сколько фильмов хотите добавить: ')
while type(ad_count_films) != int:
    try:
        ad_count_films = int(ad_count_films)
    except ValueError:
        ad_count_films = input('Введите (корректное количество) сколько фильмов хотите добавить: ')

i = 0
list_love_films = list()
love_film = str() # Только для понимания инициализировал пустую переменную строчного типа
low_films = [s.lower() for s in films]
while i < ad_count_films:
    love_film = input('Введите название фильма: ')
    if low_films.count(love_film.lower()) > 0:
        love_film = love_film[0].upper() + love_film[1:len(love_film) + 1].lower()
        list_love_films.append(love_film)
        i += 1
    else:
        print(f'Ошибка: фильма {love_film} нет :(')

del low_films
print('Ваш список любимых фильмов:\t', list_love_films)
