# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение

# Задача: предложить улучшения кода для уже решённых задач (4-5):
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Решение:

# import functools
# from random import randint

# n = int(input('Введите количество элементов списка: '))
# spisok = [randint(0, 10) for i in range(n)]
# print(spisok)
# new_spisok = [spisok[i] for i in range(len(spisok)) if i % 2 != 0]
# print(functools.reduce((lambda x, y: x+y), new_spisok))



# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Решение:

# from random import randint

# n = int(input('Введите количество элементов списка: '))
# spisok = [randint(0, 10) for i in range(n)]
# print(spisok)
# ns = list(spisok[i]*spisok[-1*(1+i)] for i in range(n//2+1*(n%2)))
# print(ns)


# 3.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Решение:

# import math

# n = int(input('Введите число N: '))
# prod_n = list(map(lambda x: math.factorial(x), range(1, n + 1)))
# print(prod_n)


# 4. Задайте список из n чисел последовательности (1+1\n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2,2,2,2,2,3] -> 13

# Решение:

# n = int(input('Введите число N: '))
# print(round(sum([((1 + 1/n)**n) for n in range(1, n+1)])))