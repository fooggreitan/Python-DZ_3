# 3.3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

a = [round(random.uniform(0,10),2) for i in range(random.randint(3,5))]

print(a)

maxFillarray = round(a[0] % 1, 2)
minFillarray = round(a[0] % 1, 2)

for i in range(len(a)):  
    if round(a[i] % 1, 2) > maxFillarray: maxFillarray = round(a[i] % 1, 2)
    elif round(a[i] % 1, 2) < minFillarray: minFillarray = round(a[i] % 1, 2)
print(f'Ответ - > {maxFillarray - minFillarray}')