# Задача 3. Счастливый билет

def checking_ticket_number(num):
    num = str(num)
    list_num = []
    for i in num:
        list_num.append(int(i))
    if sum(list_num[0:2]) == sum(list_num[3:5]):
        return 'Yes'
    return'\nNo'
num_1 = input('Введи номер билета:\t')

while type(num_1) != int :
    while len(num_1) != 6:
        num_1 = input('\nВведи корректный номер билета (6 цифр):\t')
    try:
      num_1 = int(num_1)
    except ValueError:
      num_1 = input('\nВведи корректный номер билета цифрами:\t')

print(checking_ticket_number(num_1))