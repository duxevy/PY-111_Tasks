# Задачи на зачет

1.	Оценить асимптотическую сложность приведенного ниже алгоритма:
```python
a = len(arr) - 1
out = list()
while a > 0:
    out.append(arr[a])  O(1)
    a = a // 1.7
out.merge_sort()
```

2.	Считалочка
Дано N человек, считалка из K слогов. Считалка начинает считать с первого человека. Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает. Игра происходит до тех пор, пока не останется последний человек. Для данных N и К дать номер последнего оставшегося человека.

3.	Назовем связным такой граф, в котором есть путь от любой вершины к любой другой вершине.
Дан граф, состоящий из 2+ связных подграфов, которые не связаны между собой.
Задача: посчитать число компонент связности графа, т.е. количество таких подграфов.

4.	Навигатор на сетке.
Дана плоская квадратная двумерная сетка (массив), на которой определена стоимость захода в каждую ячейку (все стоимости положительные). Необходимо найти путь минимальной стоимости из заданной ячейки в заданную ячейку и вывести этот путь.

5.	Задача консенсуса DNA ридов
При чтении DNA последовательностей могут возникать единичные ошибки, выражающиеся в неверной букве в строке. Для решения данной проблемы требуемое место читается несколько раз, после чего строится консенсус-строка, в которой на каждом месте будет стоять тот символ, что чаще всего встречался в этом месте суммарно во всех чтениях. Т.е. для строк 
ATTA
ACTA
AGCA
ACAA
консенсус-строка будет ACTA (в первой ячейке чаще всего встречалась A, во второй – C, в третьей – Т, в четвертой – снова А).
Для входного списка из N строк одинаковой длины построить консенсус-строку.

6.	Аренда ракет
Вы – компания, дающая в аренду ракеты. Каждый день к вам приходит список заявок на использование ракет в виде: (час_начала, час_конца), (час_начала, час_конца), ...
Если аренда ракеты заканчивается в час X, то в этот же час ее уже можно взять в аренду снова (т.е. час_начала может начинаться с Х).
Дано: список заявок на использование ракет
Задача: вывести ответ, хватит ли вам одной ракеты, чтобы удовлетворить все заявки на этот день
 
7.	Сорт
Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
Задача: отсортировать массив наиболее эффективным способом
