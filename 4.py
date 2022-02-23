"""
Навигатор на сетке.
Дана плоская квадратная двумерная сетка (массив), на которой определена стоимость захода в каждую ячейку (все стоимости положительные).
Необходимо найти путь минимальной стоимости из заданной ячейки в заданную ячейку и вывести этот путь.
"""

"""
Если предполагается что стоимость (вес) ячеек должен быть разным, наиболее эффективно будет использование алгоритма Дейкстры
"""

import numpy as np


def dijkstra(start_, table_):
    used = []
    d_ = np.full(n, np.inf)
    d_[start_] = 0
    p_ = list()
    for i in range(n):
        p_.append(str(i))

    while len(used) != n:
        v = None
        for x in range(n):
            if (x not in used) and ((v is None) or (d_[x] < d_[v])):
                v = x
        if d_[v] == np.Inf:
            break
        used.append(v)
        for u in range(n):
            if u == v:
                continue
            if d_[u] > d_[v] + table_[v, u]:
                d_[u] = d_[v] + table_[v, u]
                p_[u] = p_[v] + ", " + str(u)
    return d_, p_


def symmetric(a):
    return a + a.T - 2 * np.diag(a.diagonal())


#  input data
n = 20
table = symmetric(np.random.rand(n, n))

start = 0
end = n - 1
table[start, end] = 1000
table[end, start] = 1000

d, p = dijkstra(start, table)

print(d[end])  # print cost
print(p[end])  # print path
