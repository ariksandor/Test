def find_positive_and_negative(list_1):
    positive = 0
    negative = 0
    for g in list_1:
        if int(g)  > 0:
            positive += 1
        if int(g) < 0:
            negative += 1
    print('\nКоличество положительных чисел: ', positive)
    print('\nКоличество отрицательных чисел: ', negative)

i = 0
list_of_ratings = []
while i <= 3:
    list_of_ratings.append(input('Поставте свою оценку от -100 до 100:  '))
    while type(list_of_ratings[i]) != int:
      try:
        list_of_ratings[i] = int(list_of_ratings[i])
        if list_of_ratings[i] < -100 or list_of_ratings[i] > 100:
          raise ValueError
      except ValueError:
        list_of_ratings[i] = input('Поставте свою корректную оценку от -100 до 100:  ')
    i += 1

find_positive_and_negative(list_of_ratings)
