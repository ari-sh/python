
__author__ = 'Шонтукова Арина Артуровна'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruit_list = ["дыня", "апельсин", "гранат", "мандарин"]

for number, lines in enumerate(fruit_list, start = 1):
    print("{}. {:>}".format(number, lines))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list_1 = ["25", "choco", "48454", "s"]
list_2 = ["picture", "lv", "s", "25478"]
new = list(set(list_1).difference(set(list_2)))
print(new)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

s = [1, 5, 8, 4, 7]

for i in s:
    if i % 2 == 0:
        a = i / 4
    else:
        a = i * 2
    print(a)


