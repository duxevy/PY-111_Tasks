"""
Аренда ракет
Вы – компания, дающая в аренду ракеты.
Каждый день к вам приходит список заявок на использование ракет в виде: (час_начала, час_конца), (час_начала, час_конца), ...
Если аренда ракеты заканчивается в час X, то в этот же час ее уже можно взять в аренду снова (т.е. час_начала может начинаться с Х).
Дано: список заявок на использование ракет
Задача: вывести ответ, хватит ли вам одной ракеты, чтобы удовлетворить все заявки на этот день
"""

applic_list = [(1, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 6)]

sum_hours_working = 0
min_start = 0
max_end = 0
for x in applic_list:
    if x[0] < min_start:
        min_start = x[0]
    if x[1] > max_end:
        max_end = x[1]
    sum_hours_working += x[1] - x[0]

if max_end - min_start >= sum_hours_working:
    print("OK")
else:
    print("BAD")