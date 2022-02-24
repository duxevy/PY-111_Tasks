"""
Сорт
Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
Задача: отсортировать массив наиболее эффективным способом
"""

"""
Отлично справится и sorted(), поскольку использует Timsort с O(N*log(n)), но думаю ожидается другое решение :)
Поэтому написал сортировку подсчетом, наиболее эффективную для данной задачи на мой взгляд, поскольку минимальное 
и максимальное значение массива заранее известны из условия. 
"""

import random

a = 13
b = 25

array = [random.randint(a, b) for item in range(10 ** 6)]
print(array)
print(len(array))


def count_sort(arr):
    max_element = b
    min_element = a
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
    for i in range(0, len(arr)):
        count_arr[arr[i] - min_element] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]

    return arr


print(count_sort(array))
