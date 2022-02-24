"""
Считалочка Дано N человек, считалка из K слогов.
Считалка начинает считать с первого человека.
Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
Игра происходит до тех пор, пока не останется последний человек.
Для данных N и К дать номер последнего оставшегося человека.
"""

"""
РЕШЕНИЕ: 
Создается список из числа человек N. 

Далее проверям кратность слогов K количеству людей N: 
    Если K не кратно N, то выкидываем человека, стоящего по порядку равным остатку.
    Если K кратно N, то просто выкидываем последнего, т.к. считалка 100% остановится на нем.

В конце каждой итерации сокращаем кол-во человек на 1.
"""

from random import randint

N = randint(1, 50)
K = randint(1, 50)

a = list(range(N))
while N > 1:
    c = K % N
    if c == 0:
        c = N
    del a[c - 1]
    N -= 1
print(f'Остался: {a[0] + 1} человек')


