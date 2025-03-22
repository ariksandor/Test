# Задача 4. Площадь прямоугольного треугольника

def calculate_square_triangle(cat_1, cat_2):
    square = 0.5 * cat_1 * cat_2
    return f'Площадь прямоугольного треугольника: {square}'
input_cat_1, input_cat_2  = input('\nВведите длину одного катета:\t') , input('\nВведите длину другого катета:\t')

while type(input_cat_1) != float:
     try:
         input_cat_1 = float(input_cat_1)
         input_cat_2 = float(input_cat_2)
     except ValueError:
         input_cat_1, input_cat_2  = input('\nВведите корректную длину одного катета:\t') , input('\nВведите корректную длину другого катета:\t')
print(calculate_square_triangle(input_cat_1, input_cat_2))