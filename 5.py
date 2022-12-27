# 3.5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

def Fibonacci(n):
    if n in [0, 1]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

a = int(input("Введите число: "))
b = []
b.append(0)

for i in range(a):
    if i % 2 == 1: x = Fibonacci(i) * (-1)
    else: x = Fibonacci(i)
    b.append(x)
b.reverse()

for i in range(a):
    b.append(Fibonacci(i))
print(b)