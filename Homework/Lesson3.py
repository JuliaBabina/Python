# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Решение:

# from random import randint

# def get_list(a):
#     num_list = []
#     for i in range(a):
#         num_list.append(randint(-100, 100))

#     return num_list

# def sum_odd(num_list):
#     sum = 0
#     for i in range(len(num_list)):
#         if i%2 != 0:
#             sum = sum + num_list[i]

#     return sum

# n = int(input('Введите количество элементов списка: '))
# spisok = get_list(n)
# print(spisok)
# print(sum_odd(spisok))


# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Решение:

# from random import randint


# def get_list(a):
#     num_list = []
#     for i in range(a):
#         num_list.append(randint(-10, 10))

#     return num_list

# def mult_pair(list1):
#     list2 = []
#     len_list2 = 0
#     if len(list1)%2 == 0:
#         len_list2 = len(list1)//2
#     else:
#         len_list2 = len(list1)//2 + 1

#     for i in range(len_list2):
#         list2.append(list1[i]*list1[len(list1)-1-i])

#     return list2

# n = int(input('Введите количество элементов списка: '))
# spisok = get_list(n)
# print(spisok)
# print(mult_pair(spisok))


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением
#  дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Решение:

# from random import Random

# r = Random()


# def get_list(a):
#     num_list = []
#     for i in range(a):
#         num_list.append(round(r.uniform(0, 20), 2))

#     return num_list


# def calc_diff(num_list):

#     max_el = 0
#     min_el = float('inf')

#     for i in range(len(num_list)):
#         num_list[i] = round(num_list[i] % 1, 2)
#         if num_list[i] >0:
#             if num_list[i] > max_el:
#                 max_el = num_list[i]
#             if num_list[i] < min_el:
#                 min_el = num_list[i]

#     return round(max_el - min_el,2)


# n = int(input('Введите количество элементов списка: '))
# spisok = get_list(n)
# print(spisok)
# print(calc_diff(spisok))


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Решение:
    
# n = int(input('Введите десятичное число: '))
# chislo = []
# chislo.append(n % 2)
# while n//2 != 0:
#     d = n//2 % 2
#     chislo.append(d)
#     n = n//2
# chislo.reverse()
# print(*chislo,sep='')
    


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# Решение:


# def fib_pos(a):
#     pos = [0,1]
#     for i in range(2,a+1):
#         pos.append(pos[i-1]+pos[i-2])

#     return pos


# n = int(input('Введите число: '))

# list_p=fib_pos(n)

# list_n = list(reversed(list_p))
# list_n.remove(0)

# if n%2==0:
#     for i in range(len(list_n)-1):
#         if i%2==0:
#             list_n[i]=-1*list_n[i]

# else:
#     for i in range(len(list_n)-1):
#         if i%2!=0:
#             list_n[i]=-1*list_n[i]


# list_f = list_n + list_p

# print(list_f)

