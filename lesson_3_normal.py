
__author__ = 'Шонтукова Арина Артуровна'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

import math

def fibonacci(n, m):
    f = [1, 1]
    for i in range(2, n + 1,):
        f.append(f[i-1] + f[i-2])
    return f
print(fibonacci(5, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

x = []

def sort_to_max(origin_list):
    for i in range(len(origin_list)):
        x.append(min(origin_list))
        origin_list.remove(min(origin_list))
    return x
    
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_1(f, seq):
    seq_1 = [a for a in seq if f(a)]
    if type(seq) is str:     # т.к. фильтр может быть только поледовательностью, задаем условие
        seq_1 = str(seq_1)
    if type(seq) is set:
        seq_1 = set(seq_1)
    if type(seq) is tuple:
        seq_1 = tuple(seq_1)
    return seq_1
seq = (1, 5, 6, -10, 12, 36)
print(filter_1(lambda x: x < 3, seq))
   
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def par(a, b, c, d):
    ab = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    cb = math.sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
    cd = math.sqrt((d[0] - c[0])**2 + (d[1] - c[1])**2)
    ad = math.sqrt((d[0] - a[0])**2 + (d[1] - a[1])**2)
    d1 = ((a[0] + c[0])/2, (a[1] + c[1])/2)
    d2 = ((b[0] + d[0])/2, (b[1] + d[1])/2)
    if ab == cd and cb == ad and d1 == d2:
        return True
    else:
        return False
print(par((2, 4), (-3, 7), (-6, 6), (-1, 3)))