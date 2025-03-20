# Работа со списками

#basket = ['Apple' , 'Bun' , 'Cola'] # создание списка
#crate = ['Egg' , 'Fig' , 'Grape'] # создание списка
#print('Basket list: ' , basket) # вывод списка
#print('Basket Elements: ' , len(basket)) # вывод количества(размер) списка
#basket.append('Damson') # добавление вконце списка
#print('Appended: ' , basket) # вывод списка
#print('last Item Removed: ' , basket.pop() ) #вывод с удалением элемента в конце списка и возвращение удаляемое
#print('Basket List: ' , basket) #вывод списка
#basket.extend(crate) # добавление всех элементов списка в конце списка basket
#print('Extendet: ' , basket) # вывод списка
#del basket[1] # удаление елемента в списке
#print('Item Removed: ' , basket) #вывод списка
#del basket[1:3] #удаление ряда элемента списка
#print('Slice Rmoved: ' , basket) #вывод списка




# Неизменяемые списки

#zoo = ('Kangaroo' , 'Leopard' , 'Moose') # создание кортежа
#print('Tuple: ' , zoo , '\tLength: ' , len(zoo)) # Выво кортежа и ег длинны
#print(type(zoo)) # вывод типа перменной
#bag = {'Red' , 'Green' , 'Blue'} # создание множества
#bag.add('Yellow') # добавление  в произвольное место множества новый элемент
#print('\nSet: ' , bag , '\tLenght' , len(bag)) # вывод множества и его длинны
#print(type(bag)) # вывод типа переменной
#print('\nIs Green In bag Set?: ' , 'Green' in bag) # поиск элемента в множестве
#print('Is Orange In bag Set?: ' , 'Orange' in bag) # поиск элемента в множестве
#box = {'Red' , 'Purple' , 'Yellow'} # создание множества
#print('\nSet: ' , box , '\t\tLength' , len(box)) # вывод множества и его длинны
#print('Common To Both Sets: ' , bag.intersection(box)) # вывод (возвращение элементов, принадлежащих обоим множествам




# Элементы ассоциативного списка (ключ:значение)

#dict = {'name' : 'Bob' , 'ref' : ' Python' , 'sys' : 'Win'} # создание словоря
#print('Dictionary: ' , dict) # вывод словоря
#print('\nReference: ' , dict["ref"]) # вывод элемента по ссылке ключа
#print('\nKeys: ' , dict.keys()) # вывод ключей словоря
#del dict['name'] # удаление елемента с ключем
#dict['user'] = 'Tom' # добавления ключ: элемент всловарь
#print('\nDictionary: ' , dict) # вывод словаря
#print('\nIs There A name key? :' , 'name' in dict) # вывод результата поиска ключа name




# Ветвление с помощью условного оператора

#Задача полиндром
'''def checking_for_palindromes(slovo):
   if slovo[::-1].lower() == slovo.lower():
       return '\nМожно сделать палиндромом, сцука'
   return '\nНельзя сделать палиндромом, сцука'
slovo = str(input('Введите слово для проверки: '))
print(checking_for_palindromes(slovo))'''
def is_poly(string):
    # Создаем словарь для подсчета количества вхождений каждогосимвола

    char_dict = dict()

# Проходим по каждому символу в строке
    for i_sym in string:
    # Увеличиваем счетчик для текущего символа

            char_dict[i_sym] = char_dict.get(i_sym, 0) + 1

# Переменная для подсчета символов с нечетным количеством вхождений

    odd_count = 0

# Проходим по значениям словаря (количеству вхождений символов)

    for i_value in char_dict.values():

    # Если количество вхождений нечетное, увеличиваем счетчик нечетных
        if i_value % 2 != 0:
            odd_count += 1
        # Палиндром может быть составлен, если не более одного символа имеет нечетное количество вхождений

    return odd_count <= 1

# Запрашиваем у пользователя ввод строки
my_string = input('Введите строку: ')
my_string = my_string.lower()
# Проверяем, можно ли сделать палиндром из введенной строки
if is_poly(my_string):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')





