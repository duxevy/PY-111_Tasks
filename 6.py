"""
Аренда ракет
Вы – компания, дающая в аренду ракеты.
Каждый день к вам приходит список заявок на использование ракет в виде: (час_начала, час_конца), (час_начала, час_конца), ...
Если аренда ракеты заканчивается в час X, то в этот же час ее уже можно взять в аренду снова (т.е. час_начала может начинаться с Х).
Дано: список заявок на использование ракет
Задача: вывести ответ, хватит ли вам одной ракеты, чтобы удовлетворить все заявки на этот день
"""

orders_list1 = [(1, 2), (2, 4), (4, 5), (6, 7), (7, 9), (9, 12)]
orders_list2 = [(1, 2), (1, 4), (3, 5), (2, 7), (5, 9), (7, 14)]
checked_orders = []


def rent(orders_list, checked_orders):
    flag = True
    checked_orders = []
    for first_order in orders_list:
        first_order_working_hours = range(first_order[0], first_order[1])
        if flag:
            for next_order in orders_list:
                if first_order == next_order or \
                        next_order in checked_orders:
                    pass
                else:
                    if next_order[0] in first_order_working_hours:
                        flag = False
                    if next_order[1] in first_order_working_hours:
                        flag = False
                    if first_order[0] in range(next_order[0], next_order[1] + 1):
                        flag = False

        checked_orders.append(first_order)

    if flag:
        print('Одной ракеты хватит')
    else:
        print('Одной ракеты не хватит')


rent(orders_list1, checked_orders)  # enough
rent(orders_list2, checked_orders)  # not enough
