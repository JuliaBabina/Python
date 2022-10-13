# 1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter.
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.

# st = '2 32 34 5 43 2 4 34'.split()
# res = list(filter(lambda x: len(x) == 2, st))
# print(res)

# от Сергея******************************************

# print(*filter(lambda x: len(str(abs(int(x)))) == 2, input().split()))

# ******************************************

# arr = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
# print(list(filter(lambda e: 9 < e < 100, arr)))



# 2. Дан список, вывести отдельно буквы и цифры.

# от Сергея******************************************

# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')


# b= filter(str.isalpha, a)
# c= filter(str.isdigit, a)

# print(*b)
# print(*c)



# 3. Преобразовать набора списков
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор

# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]

# и потом вернуть в исходное состояние

# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]

# от Сергея******************************************

# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]

# a,b,c = map(list,zip(users, ids, salary))
# print(a,b,c, sep="\n")
# a,b,c= map(list,zip(a,b,c))

# print(a,b,c, sep="\n")

# ******************************************


# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]

# for i in zip(users, ids, salary):
# print(i)

# users_1, ids_1, salary_1 = map(list, zip(*zip(users, ids, salary)))

# print(users_1,ids_1,salary_1+ '\n')


# Разбор ДЗ к 4 семинару


# 1. Вычислить число c заданной точностью *d*
# *Пример:*
# - при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$

# qnt = int(input("Input the number of decimal places: "))

# pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095

# pi_for_user = round(pi, qnt+1)

# for i in range(qnt):
# pi_for_user *= 10

# pi_for_user = math.trunc(pi_for_user)

# while pi_for_user > 10:
# pi_for_user /= 10

# print(round(pi_for_user, qnt))


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# list = []
# user_num = abs(int(input("Input a number: ")))

# for i in range(2, user_num + 1):
# while user_num % i == 0:
# list.append(i)
# user_num //= i
# if user_num > 1 and user_num % i != 0:
# list.append(user_num)
# user_num //= user_num
# print(list)

# от Сергея******************************************

# n = int(input("Введите число N: "))
# i = 2
# list = []

# while i <= n:
# if n % i == 0:
# list.append(i)
# n //= i
# i = 2
# else:
# i += 1
# print(f"Простые множители введенного числа указаны в списке: {list}")

# от Макса******************************************

# numb = int(input('input number: '))
# simple_numbers_list = [2, 3, 5, 7]
# simple_numbers_list = simple_numbers_list + [i for i in range(7, numb+1, 2) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0]
# simple_numbers_list.reverse()
# result_list = []
# for i in simple_numbers_list:
# while numb % i == 0:
# numb = numb/i
# result_list.append(i)
# print(f'list of prime factors of number {numb} : {result_list}')


# ******************************************

# def simple(n):
# for i in range(2, n + 1):
# if not n % i:
# mults.append(i)
# simple(int(n / i))
# break

# string = input("Введите целое число: ")

# if not string.isdigit():
# print("Неверный ввод данных")
# exit()

# num = int(string)
# mults = []

# simple(num)
# if num == 1:
# mults.append(1)
# print(f"{num} = {mults[0]}", end = "")
# for i in range(1, len(mults)):
# print(f" * {mults[i]}", end = "")


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# от Сергея ******************************************

# def elements(nums):
# nums = [int(i) for i in nums.split()]
# return list(set(nums))

# numbers = '1 1 2 2 3 455 66 66 2 1'
# print(elements(numbers))

# ******************************************

# inp_list = list(map(int, input('Введите числа через пробел: ').split()))
# print(inp_list)
# targets=[]
# for i in range(len(inp_list)):
# if inp_list.count(inp_list[i])>1:
# targets.append(i)
# for i in range(len(inp_list)):
# if i in targets:
# print('',end=' ')
# else:
# print(inp_list[i],end=' ')


# ******************************************

# a=list(map(int,input().split()))
# new_list = []
# for i in a:
# if a.count(i) == 1:
# new_list.append(i)
# print(new_list)


# от Сергея ******************************************

# b = [1, 1, 2, 3, 3, 4, 5]
# a = []
# for i in b:
# if b.count(i) == 1:
# a.append(i)

# print(a)

# ******************************************

# list = [5, 6, 8, 5, 8, 10, 5]
# list1 = []
# count = 0
# for i in range(len(list)):
# while count < len(list):
# if list[count] == list[i] and count != i:
# count = 0
# break
# count +=1
# else:
# list1.append(list[i])
# count = 0
# print(list1)


# ******************************************

# arr = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
# elems = {}
# uniq = []

# for i in arr:
# if elems.get(i):
# elems[i] += 1
# else:
# elems[i] = 1
# uniq = list(filter(lambda e: elems[e] == 1, elems))

# print(f"Уникальные числа: {uniq}")

# ******************************************


# numb_list = list(map(int, input('input numbers: ').split()))
# list = [i for i in numb_list if numb_list.count(i) == 1],
# print(list)

# ******************************************

# import random
# # Create a list of random size between 3 and 10, filled with random
# # integers between -10 and 10.
# list1 = [random.randint(-10, 10) for i in range(random.randrange(3, 10))]
# print(list1)
# list2 = [i for i in list1 if list1.count(i) == 1]
# print(list2)



# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# От Сергея*******************************************************************

# from random import randint

# k = int(input('Insert equation power: '))
# koefs = list()
# for i in range(1, k + 2):
# koefs.append(randint(1, 100))

# ans = list()
# for i in range(len(koefs)):
# if k == 1:
# ans.append(f'{koefs[i]}*x')
# elif k == 0:
# ans.append(f'{koefs[i]}')
# else:
# ans.append(f'{koefs[i]}*x**{k}')
# flag = randint(0, 1)
# if flag == 1:
# ans.append('+')
# elif flag == 0:
# ans.append('-')
# k -= 1

# ans.pop(-1)
# ans.append('=0')
# fout = open('output.txt', 'w')
# fout.write(''.join(ans))
# fout.close()

# *******************************************************************


# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# от Сергея ******************************************(если длина многочленов равна)

# ffile1 = open('file1.txt', 'r')
# ffile2 = open('file2.txt', 'r')
# ffile3 = open('file3.txt', 'w')
# file1 = ffile1.readline()
# file2 = ffile2.readline()
# for i in range(len(file1)):
# if file1[i-1] != '^':
# if file1[i].isnumeric():
# ffile3.write(str(int(file1[i])+int(file2[i])))
# else:
# ffile3.write(str(file1[i]))
# else:
# ffile3.write(str(file1[i]))
# ffile1.close
# ffile2.close
# ffile3.close

# от Сергея ******************************************

# import random
# def nmnogochlen1(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:

# if b > 0:
# res += '+' + str(b) + '*x'
# if c > 0:
# res += '+' + str(c)
# return f'{a}*x^2' + res


# def nmnogochlen2(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
# if b > 0:
# res += '+' + str(b) + '*x'
# if c > 0:
# res += '+' + str(c)
# return f'{a}*x^2' + res


# f = open('dz40.txt', 'w')
# f.write(nmnogochlen1())
# print(nmnogochlen1())
# f.close()

# f = open('dz41.txt', 'w')
# f.write(nmnogochlen2())
# print(nmnogochlen2())
# f.close()


# f = open('dz40.txt', 'r')
# list_5 = str(f.readline()).split('x')
# c1 = b1 = a1 = 0
# if len(list_5) == 3:
# c1 = list_5[2][1:]
# if len(list_5) >= 2:
# b1 = list_5[1][3:-1]
# a1 = list_5[0][:-1]
# f.close()

# f = open('dz41.txt', 'r')
# list_51 = str(f.readline()).split('x')
# c2 = b2 = a2 = 0
# if len(list_51) == 3:
# c2 = list_51[2][1:]
# if len(list_51) >= 2:
# b2 = list_51[1][3:-1]
# a2 = list_51[0][:-1]
# f.close()

# f = open('dz42.txt', 'w')
# f.write(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))

# print(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
# f.close()