# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
# n = int(input("Введите произвольную длину n массива: "))
n = 30
list1 = []
result = []
for i in range(n):
    list1.append(random.randint(1, 100))
print(f"Наш массив из {n} элементов: {list1}")
min, max = map(int, input(
    "Задайте двумя числами (min и max) диапазон значений массива через пробел: ").split(" "))
print(min, max)
for i in range(n):
    if min <= list1[i] <= max:
        result.append(i)
print(
    f"Индексы чисел массива из выбранного диапазона от {min} до {max} : {result}")
