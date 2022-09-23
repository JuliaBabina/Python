# Задачи:

# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
    
#     *Примеры:* 
    
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет


# a = int (input('Введите число a: '))
# b = int (input('Введите число b: '))


# if a*a==b:
#     print ('Да')
# elif b*b==a:
#     print ('Да')
# else:
#     print ('Нет')   

# ИЛИ

# a = int(input('Введите число a '))
# b = int(input('Введите число b '))

# if a*a==b:
#     print (f'- {a}, {b} -> да')

# elif b*b==a:
#     print (f'- {a}, {b} -> да')

# else:
#     print (f'- {a}, {b} -> нет')


#ИЛИ

# a = int (input("введите a: "))
# b = int (input("введите b: "))
# if a*a == b or b*b==a:
#     print ("да")
# else:
#     print ("нет")




# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90


# a = int (input('Введите число a: '))
# b = int (input('Введите число b: '))
# c = int (input('Введите число c: '))
# d = int (input('Введите число d: '))
# e = int (input('Введите число e: '))

# max1 = a      #просто max не использовать!! это функция стандартная

# if b>max1:
#     max1 = b
# if c>max1:
#     max1 = c
# if d>max1:
#     max1 = d
# if e>max1:
#     max1 = e

# print(max1)

#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#    
#    Примеры:
#    
#    - 1, 4, 8, 7, 5 -> 8
#    - 78, 55, 36, 90, 2 -> 90
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# num4 = int(input("Введите четвертое число: "))
# num5 = int(input("Введите пятое число: "))

# arr = [num1, num2, num3, num4, num5]
# numMax = num1

# for i in arr:
#     if numMax < i:
#         numMax = i
# print(numMax)

# ИЛИ


# fiver = list(map(int, input('Введите 5 чисел через пробел: ').split()))
# max=fiver[0]
# for i in range(len(fiver)):
#     if fiver[i]>max:
#         max=fiver[i]
# print(max)

# ИЛИ


# numbers = int(input(' input amount of numbers:  '))
# count = 1
# arr = []
# while( count <= numbers):
#     num = int(input(f"input {count} number: "))
#     arr.append(num)
#     count += 1 
# print (arr)
# max_num = arr[0]
# for i in arr:
#     if i > max_num:
#         max_num = i

# print(f' max number is: {max_num}')

# ИЛИ

# a=[1, 4, 8, 7, 5]
# print(max(1, 4, 998, 7, 5))

# ИЛИ

# a = int (input("введите a: "))
# b = int (input("введите b: "))
# c = int (input("введите c: "))
# d = int (input("введите d: "))
# e = int (input("введите e: "))

# m = a
# for i in b,c,d,e:
#     if i>m: m=i
# print(m)



# **Задачи 2 блок:**

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
#     *Примеры:* 
    
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5


# n = int (input("введите число N: "))
# print (list(range(-n, n + 1)))

#ИЛИ

# N = int (input("введите число N: "))
# for i in range(-N, N +1):
#     print(i, end = " ")


# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# Все фигня, порешать

# print(int((float(input())*10) % 10))

# ИЛИ

# f = float(input())
# d = int( (f*10) % 10 )
# print(f, d, sep=" -> ")

#ИЛИ вариант преподавателя

# num = float(input("Введите дробное число: "))

# result = int((num*10) % 10)
# if result:
#     print(num, result, sep=" -> ")
# else:
#     print(num, "нет", sep=" -> ")


# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# n = int(input())
# b = (n % 5 == 0 and n % 10 ==0 or n % 15 == 0) and not n % 30 == 0
# print(n, b, sep=" -> ")


# 2 и 3 порешать в ДЗ







