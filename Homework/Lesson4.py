# Урок 4. Данные, функции и модули в Python. Продолжение

# 1. Вычислить число c заданной точностью d
# пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# Решение:

# from cmath import pi
# from decimal import Decimal

# d = input('Введите точность огругления в формате "0.001", где точность округления - это количество знаков после запятой: ')
# print(f'Число Пи: {pi}')
# num = Decimal(d).as_tuple().exponent*(-1)
# print(f'Число Пи с {num} зн. после запятой: {round(pi, num)}')



# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# Решение:

# n = int(input('Введите число N: '))

# i = 2
# spisok = []
# while i <= n:
#     if n % i == 0:
#         spisok.append(i)
#         n //= i
#     else:
#         i += 1
# print(spisok)
 


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Решение:

# spisok = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
# spisok_2 = []
# [spisok_2.append(i) for i in spisok if i not in spisok_2]
# print(f'Неповторяющиеся элементы исходной последовательности: {spisok_2}')



# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# Решение:


# from random import Random


# def get_kf(n):
#     r = Random()  
#     spisok = [r.randint(0,101) for i in range(n+1)]
#     return spisok

# def create_pol(ls):
#     spisok = ls[::-1]
#     wr = ''
#     if len(spisok)<1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(spisok)):
#             if i != len(spisok) - 1 and spisok[i] != 0 and i != len(spisok) - 2:
#                 wr += f'{spisok[i]}x^{len(spisok)-i-1}'
#                 if spisok[i+1] != 0:
#                     wr += ' + '
#             elif i == len(spisok) - 2 and spisok[i] != 0:
#                 wr += f'{spisok[i]}x'
#                 if spisok[i+1] != 0:
#                     wr += ' + '
#             elif i == len(spisok) - 1 and spisok[i] != 0:
#                 wr += f'{spisok[i]} = 0'
#             elif i == len(spisok) - 1 and spisok[i] == 0:
#                 wr += ' = 0'
#     return wr

# k = int(input('Введите натуральную степень: '))
# kf = get_kf(k)
# print(create_pol(kf))

# with open('L4-4.txt', 'w') as data:
#     data.write(create_pol(kf))


# 5.Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# Решение:


# from random import Random


# def get_kf(n):
#     r = Random()  
#     spisok = [r.randint(0,101) for i in range(n+1)]
#     return spisok

# def create_pol(ls):
#     spisok = ls[::-1]
#     wr = ''
#     if len(spisok)<1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(spisok)):
#             if i != len(spisok) - 1 and spisok[i] != 0 and i != len(spisok) - 2:
#                 wr += f'{spisok[i]}x^{len(spisok)-i-1}'
#                 if spisok[i+1] != 0:
#                     wr += ' + '
#             elif i == len(spisok) - 2 and spisok[i] != 0:
#                 wr += f'{spisok[i]}x'
#                 if spisok[i+1] != 0:
#                     wr += ' + '
#             elif i == len(spisok) - 1 and spisok[i] != 0:
#                 wr += f'{spisok[i]} = 0'
#             elif i == len(spisok) - 1 and spisok[i] == 0:
#                 wr += ' = 0'
#     return wr



# def k_pol(k):
#     if 'x^' in k:
#         i = k.find('^')
#         num = int(k[i+1:])
#     elif ('x' in k) and ('^' not in k):
#         num = 1
#     else:
#         num = -1
#     return num


# def kf_pol(k):
#     if 'x' in k:
#         i = k.find('x')
#         num = int(k[:i])
#     return num

# def to_pol(st):
#     st = st[0].replace(' ', '').split('=')
#     st = st[0].split('+')
#     lst = []
#     l = len(st)
#     k = 0
#     if k_pol(st[-1]) == -1:
#         lst.append(int(st[-1]))
#         l -= 1
#         k = 1
#     i = 1 
#     ii = l-1 
#     while ii >= 0:
#         if k_pol(st[ii]) != -1 and k_pol(st[ii]) == i:
#             lst.append(kf_pol(st[ii]))
#             ii -= 1
#             i += 1
#         else:
#             lst.append(0)
#             i += 1
        
#     return lst

# k = int(input('Введите натуральную степень для первого многочлена: '))
# l = int(input('Введите натуральную степень для второго многочлена: '))
# kf_k = get_kf(k)
# kf_l = get_kf(l)
# print(create_pol(kf_k))
# print(create_pol(kf_l))

# with open('L4-5-1.txt', 'w') as data:
#     data.write(create_pol(kf_k))
# with open('L4-5-2.txt', 'w') as data:
#     data.write(create_pol(kf_l))

# with open('L4-5-1.txt', 'r') as data:
#     p1 = data.readlines()
# with open('L4-5-2.txt', 'r') as data:
#     p2 = data.readlines()

# print(p1)
# print(p2)

# sp1 = to_pol(p1)
# sp2 = to_pol(p2)
# ll = len(sp1)
# if len(sp1) > len(sp2):
#     ll = len(sp2)
# sp3 = [sp1[i] + sp2[i] for i in range(ll)]
# if len(sp1) > len(sp2):
#     mm = len(sp1)
#     for i in range(ll,mm):
#         sp3.append(sp1[i])
# else:
#     mm = len(sp2)
#     for i in range(ll,mm):
#         sp3.append(sp2[i])

# print(create_pol(sp3))

# with open('L4-5-3.txt', 'w') as data:
#     data.write(create_pol(sp3))



