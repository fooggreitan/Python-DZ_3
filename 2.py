# 3.2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

a = input("Введите числа: ").split(",")
b = [] 
for i in range((len(a) + 1)//2):
    b.append(int(a[i]) * int(a[int(len(a)) - 1 - i]))
print(b)
