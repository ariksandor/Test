dict_1 = {
    'пванов' : 'и',
    'иетров' : 'а'
}
sorted_dict = dict(sorted(dict_1.items(), key=lambda item: item[1]))
print(list(dict_1.keys())[0])
print(sorted_dict)


