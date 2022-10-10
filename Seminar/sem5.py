# Доп задания 5 семинар

# Сергей Сердюк: 
# 1. НОД (наибольший общий делитель)

# Код от Сергея

# a=20
# b=58

# if a < b :
# a, b = b, a

# while b!=0:
# a, b = b, a % b

# print(a)

# ИЛИ ***************************

# a=20
# b=58

# while a != b:
# if a > b:
# a -= b
# else:
# b -= a

# print(a)

# *******************************************************



# Сергей Сердюк: 
# 2. Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr". 
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.


# от Сергея:

# print((lambda x: 'ra' in x)(input()))

# ИЛИ *****************

# contains = lambda s, sample='ra': sample in s
# s = input()
# print(contains(s))



# 3. АНТОН


# N = int(input("Введите количество холодильников: "))
# refregerators = []
# for i in range(N):
# refregerators.append(str(input()))
# print("Заражены холодильники с номерами:")
# for i in range(N):
# if refregerators[i].find('a') != -1:
# if refregerators[i].find('n', refregerators[i].find('a')) != -1:
# if refregerators[i].find('t', refregerators[i].find('n')) != -1:
# if refregerators[i].find('o', refregerators[i].find('t')) != -1:
# if refregerators[i].find('n', refregerators[i].find('o')) != -1:
# print(i + 1, end = " ")
# print()

# *******************************************************


# fridges = ["9", "osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen", "anton", "aoooooooooontooooo", "elelelelelelelelelel", "ntoneeee", "tonee", "253235235a5323352n25235352t253523523235oo235523523523n", "antoooooooooooooooooooooooooooooooooooooooooooooooooooon", "unton"]
# word = 'anton'
# count = 0
# number = 0

# print("Заражены", end = " ")
# for text in fridges:
# for char in text:
# if char == word[count]:
# count += 1
# if count == len(word):
# print(f'{number}', end = " ")
# break
# number += 1
# count = 0

# *******************************************************

# от Сергея:

# for i in range(int(input())):
# s, virus, x = input(), 'anton', 0
# for sym in s:
# if sym == virus[x]:
# x += 1
# if x == 5:
# print(i + 1, end=' ')
# break

# *******************************************************

# data = "C:\\Users\\МSI\\Desktop\\Python for n00bz\\seminars\\sem3\\fridges.txt"
# busted_serialNumbers=[]
# k=0
# with open(data,'r') as f:
# for i in f:
# if 'a' in i:
# if 'n' in i:
# if 't' in i:
# if 'o' in i:
# if 'n' in i:
# busted_serialNumbers.append(k)
# k+=1
# print(busted_serialNumbers)


# Разбор ДЗ c 3 семинара

# Сергей Сердюк: 
# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# nums = list(map(int, input("Задайте список из нескольких чисел через пробел: ").split()))
# odds = []
# sum = 0

# for i in range(1, len(nums), 2):
# odds.append(nums[i])
# sum += nums[i]

# print(f'{nums} -> на нечётных позициях элементы {odds}, ответ: {sum}')

# *******************************************************

# list = [2, 3, 5, 9, 3]
# sum = 0
# for i in range(1, len(list), 2):
# sum = sum + list[i]
# print(sum)

# *******************************************************

# import random

# size = int(input('Введите число: '))
# numeros = []
# sum=0
# for i in range (size):
# numeros.append(random.randint(0,11))
# if i%2 == 1:
# sum+=numeros[i]
# print(numeros, '\n', sum)

# *******************************************************

# my_list = [8, 5, 7, 3, 6]
# print(sum(my_list[1::2]))


# *******************************************************

# import random
# a = [random.randint(-5,5) for _ in range(10)]
# print(a)
# sum=0
# for i in range (len(a)+1):
# if i%2!=0:
# sum=sum+a[i]
# print (sum)

# *******************************************************

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# import math

# nums = list(map(int, input("Задайте список из нескольких чисел через пробел: ").split()))
# mult = []

# for i in range(math.ceil(len(nums)/2)):
# mult.append(nums[i] * nums[-i-1])

# print(f'{nums} => {mult}')

# *******************************************************

# import random

# size = int(input('Введите число: '))
# numeros = []
# couple_product = []
# for i in range (size):
# numeros.append(random.randint(0,11))
# if size%2==0:
# for i in range (size//2):
# couple_product.append(numeros[i]*numeros[size-1-i])
# else:
# for i in range (size//2+1):
# couple_product.append(numeros[i]*numeros[size-1-i])
# print(numeros, '\n', couple_product)

# ******************************************************* от Сергея

# import random
# b = int(input('Введите кол-во чисел в списке for 2# = '))
# list_b = list(random.randint(0, 10) for i in range(b))
# print(list_b)
# proiz_b = list(list_b[i]*list_b[-1*(1+i)] for i in range(b//2+1*(b%2)))
# print(proiz_b)


# 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random

# def FindMax (inp_list):
# max=inp_list[0]
# for i in range (len(inp_list)):
# if inp_list[i]>max:
# max=inp_list[i]
# return max

# def FindMin (inp_list):
# min=inp_list[0]
# for i in range(len(inp_list)):
# if inp_list[i]<min:
# min=inp_list[i]
# return min

# size = int(input('Введите число: '))
# numeros = []
# nums=[]
# result=0

# print('Ваша последовательность: ')
# for i in range (size):
# numeros.append(random.randint(0,11)+round(random.random(),2))
# print(numeros[i], end=' ')
# num=round(numeros[i] - int(numeros[i]),2)
# nums.append(num)

# min_el=FindMin(nums)
# max_el=FindMax(nums)
# result=round(min_el+max_el,2)
# print ('Сумма максимальной и минимальной дробной части: ', result)

# # ******************************************************* 

# import math

# list = [1.7, 1.2, 3.1, 5.3, 10.01]

# min_elem = math.inf
# max_elem = - math.inf

# for i in range(len(list)):
# if list[i] % 1 < min_elem:
# min_elem = list[i] % 1
# elif list[i] % 1 > max_elem:
# max_elem = list[i] % 1
# print(f'{round(max_elem, 3)} - {round(min_elem, 3)} = {round(max_elem - min_elem, 3)}')

# # ******************************************************* 

# nums = list(map(float, input("Задайте список из нескольких чисел через пробел: ").split()))
# min_frac = 1
# max_frac = 0

# for i in nums:
# frac = round(i % 1, 2)
# if frac:
# if max_frac < frac:
# max_frac = frac
# if min_frac > frac:
# min_frac = frac
# # print(f'frac = {frac}: min_frac = {min_frac}; max_frac = {max_frac}')

# print(f'{nums} -> {max_frac - min_frac}')

# # ******************************************************* от Сергея

# list = [1.1, 1.2, 3.1, 10.01]
# mix_list = []

# for i in list:
# mix_list.append(round(i-int(i), 2))

# print(list, end=' => ')
# print(max(mix_list) - min(mix_list))


# Сергей Сердюк: 
# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# num = int(input("Введите число: "))
# binum = ''

# while num:
# binum = str(num%2) + binum
# num //= 2

# print(binum)

# # ******************************************************* от Сергея

# a=int(input('Введите число = '))
# print(bin(a))

# # *******************************************************

# number = int(input('Введите число: '))
# ones_and_zeros=[]
# while number>0:
# ones_and_zeros.append(number%2)
# number//=2
# for i in range(len(ones_and_zeros)):
# print(ones_and_zeros[len(ones_and_zeros)-1-i], end='')


# # ******************************************************* от Сергея

# a = int(input('введите число для перевода = '))
# b = ''
# while a != 0:
# b = str(a % 2) + b
# a = a // 2
# print(b)

# # *******************************************************

# n = int(input("Введите число: "))
# b = ''
# while n > 0:
# b = str(n % 2) + b
# n = n // 2
# print(f'Число в двоичной системе {b}')


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# def Fib (n):
# if n==1 or n==2:
# return 1
# else:
# return Fib(n-1)+Fib(n-2)

# def NFib (n):
# if n == -1:
# return 1
# elif n==-2:
# return -1
# else:
# return NFib(n+2)-NFib(n+1)

# def Reverse (inp_list):
# for i in range(len(inp_list)//2):
# inp_list[i], inp_list[len(inp_list)-1-i] = inp_list[len(inp_list)-1-i], inp_list[i]

# number = int(input('Введите число: '))
# pos_fib = []
# neg_fib = []
# for i in range (1, number+1):
# pos_fib.append(Fib(i))
# neg_fib.append(NFib(-i))
# Reverse(neg_fib)
# neg_fib.append(0)
# print(number,'->',neg_fib+pos_fib)


# #  *******************************************************


# n = int(input('Введите длину ряда: '))
# list_Fibanachi = []
# def Fibonacci(x):
# if x == 0:
# return 0
# if x == 1:
# return 1
# if x > 0:
# return (Fibonacci(x - 1) + Fibonacci(x - 2))
# if x < 0:
# return (Fibonacci(x + 2) - Fibonacci(x + 1))

# for i in range(-n,n + 1):
# list_Fibanachi.append(Fibonacci(i))
# print(list_Fibanachi)

# # *******************************************************

# N = int(input("Введите целое число: "))
# Fibonacci = [0, 1]
# for i in range(-N, 0):
# Fibonacci.append((-1) ** (-i + 1) * Fibonacci[-i])
# for i in range(2, N + 1):
# Fibonacci.append(Fibonacci[i - 1] + Fibonacci[i - 2])
# print(Fibonacci)



# #  *******************************************************

# import math
# b = abs(int(input('Введите число:')))
# kod = []
# for i in range(-b,b+1):
# kod.append(i)
# for i in range(-b-2,-len(kod)-1,-1):
# kod[i]=kod[i+2]-kod[i+1]
# for i in range(b+2,len(kod),1):
# kod[i]=kod[i-2]+kod[i-1]
# print(kod)


# #  ******************************************************* от Максима Шульги

# def nega_fibonacci(numb):
# array = [1, 0, 1]
# for i in range(1, numb):
# array.insert(0, array[1] - array[0])
# array.append(array[-2] + array[-1])
# return array


# num = int(input('input number: '))
# print(nega_fibonacci(num))



#  *******************************************************




#  *******************************************************