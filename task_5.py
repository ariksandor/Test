i = 0
list_of_ratings = []
while i <= 6:
    list_of_ratings.append(input('Поставте свою оценку от -100 до 100'))
    while list_of_ratings[i] != int:
      try:
        list_of_ratings[i] = int(list_of_ratings[i])
      except ValueError:
        list_of_ratings.append(input('Поставте свою корректную оценку от -100 до 100'))
    i =+ 1
#print(list_of_ratings)

