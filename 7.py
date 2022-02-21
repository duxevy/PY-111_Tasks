"""
Сорт
Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
Задача: отсортировать массив наиболее эффективным способом
"""

import numpy as np
import random

a = 13
b = 25
array = list([x + a for x in (range(b - a))]) * 2
random.shuffle(array)
print(array)

numbers = np.full(b - a, 0)
for x in array:
    numbers[x - a] += 1
result = np.array([], dtype=int)
for i in range(b - a):
    result = np.concatenate((result, np.full(numbers[i], a + i, dtype=int)))
print(np.array(result))
