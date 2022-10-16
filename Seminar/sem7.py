# Сергей Сердюк: 1.напечатать сторку в одну линию - C:\WINDOWS\System32\drivers\etc\nst

# print('ваша строка: ', 'C:\\WINDOWS\System32\\drivers\\etc\\nst')

# *************************от Сергея

# print(r'C:\WINDOWS\System32\drivers\etc\nst')

# Сергей Сердюк: 2. записать в список все буквы строки f=‘privet’

# f='privet'
# result = [i for i in f]
# print(result)

# *************************от Сергея

# print(sorted("privet"))

# ************************

# f='privet'
# new_list = list(f)
# print(new_list)


# Сергей Сердюк: 3. преобразовать список таким образом
# Сергей Сердюк: a = [4, 3, -10, 1, 7, 12]
# Сергей Сердюк: [4, -10, 12, 3, 1, 7]
# Сергей Сердюк: выход

# a = [4, 3, -10, 1, 7, 12] -> [4, -10, 12, 3, 1, 7]

# a = [4, 3, -10, 1, 7, 12]
# b = [i for i in a if i%2==0]
# c = [i for i in a if i%2!=0]
# print(a,'->', b+c)

# *************************от Сергея

# a = [4, 3, -10, 1, 7, 12]
# a.sort(key=lambda x: x%2)
# print(a)

# *************************

# a = [4, 3, -10, 1, 7, 12]
# a.sort(key=lambda x: x % 2 == 0, reverse=True)
# print(a)

# *************************

# l.sort(key= lambda x: len(x), reverse=True)
# print(*l)



# Сергей Сердюк: 3)На вход программы поступает список наименований рек, записанных в одну строчку через пробел. 
# Необходимо отсортировать этот список в порядке убывания длин названий. Результат вывести в одну строчку через пробел.

# Sample Input:
# Лена Енисей Волга Дон
# Sample Output:
# Енисей Волга Лена Дон


# rivers = input('Введите список рек через пробел: ')
# rivs = list(rivers.split())
# len_riv=[]
# for i in rivs:
#     len_riv.append(len(i))
# result = list(zip(rivs, len_riv))
# result.sort(key=lambda x: x[1], reverse=True)
# print(result)

# *************************от Сергея


# s=sorted(input().split(), key=lambda x: len(x))[::-1]
# print(*s)

# *************************

# l.sort(key= lambda x: len(x), reverse=True)
# print(*l)

# *************************

# rivers.sort(key=lambda x: len(x), reverse=True)


# Сергей Сердюк: 4) Вводится строка. Требуется, используя введенную строку, сформировать N=10 пар кортежей в формате:
# (символ, порядковый индекс)
# Первый индекс имеет значение 0. Строка может быть короче 10 символов, а может быть и длиннее. То есть, число пар может быть 10 и менее. 
# Используя функцию zip сформируйте указанные кортежи и сохраните в список с именем lst.


# inp_string = input('')
# zipper = [i for i in range(11)]
# result = list(zip(inp_string,zipper))
# print(*result)

# *************************от Сергея

# s = input()
# lst = list(zip(s, range(10)))
# print(lst)

# *************************

# n = 10
# lst = []
# for i in zip(range(0,n+1),input('введите текст: ')):
# lst.append(i)
# print(lst)

# *************************

# f_l = 'ткива'
# f_list = [(x) for x in enumerate(f_l) if x[0] < 10]
# print(f_list)



# Сергей Сердюк: 4. Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.
# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.

# l_value = [23, 63, 2, 81 ,34, 234]
# l_value = filter(lambda x: (9 < x < 100) and (x % 9 == 0), l_value)
# l_value = map(lambda x: x**2, l_value)
# print(sum(l_value))

# *************************

# input = list(filter(lambda x: x % 9 == 0, list(range(10,100))))
# input = list(map(lambda x: x**2, input))
# input_sum = sum(input)

# *************************от Сергея

# l = [i for i in range(10, 100)]
# l1 = list(filter(lambda x: x % 9 == 0, l))
# l2 = sum(list(map(lambda x: x**2, l1)))
# print(l2)

# *************************

# kombination = [x**2 for x in range(10,100) if not x%9]
# print(sum(kombination))


# Сергей Сердюк: 5. Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков и определяет, можно ли из этих отрезков составить треугольник.
# Входные данные
# Выходные данные
# triangle(1, 1, 2)
# Это не треугольник
# triangle(7, 6, 10)


# triangle = lambda a,b,c: print('Это треугольник') if a+b>c and c+b>a and a+c>b else print('Это не тругольник')
# triangle(7,6,10)
# triangle(1, 1, 2)

# *************************

# def tr(a, b, c):
# return a + b > c and b + c > a and a + c > b
# print(tr(1, 2, 3))

# *************************

# def triangle(a, b, c):
# if a + b > c and b + c > a and c + a > b:
# print('треугольнику быть')
# else:
# print('нет')

# print(triangle(7,6,10))

# *************************


# triangle = [1,1,2]
# triangle.sort()
# is_triangle = triangle[0] + triangle[1] > triangle[2]

# if is_triangle:
# print('Это треугольник!')
# else:
# print('Это не треугольник!')

# *************************



# Разбор дз с семинара 5

# Крестики-нолики

# Максим Шульга: def win_combination(list):
# one = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
# [3, 6, 9], [2, 5, 8], [1, 5, 9], [3, 5, 7]]
# count = 0
# for i in one:
# for n in i:
# for k in list:
# if n == k:
# count += 1
# if count >= 3:
# return True
# count = 0

# RLE

# Abbos Atamuratov: 

# text = input('Введите строку: ')

# def Squash(inp_text):
# result = []
# i=0
# while i in range(len(inp_text) - 1):
# counter = 1
# key = inp_text[i]
# for j in range(i + 1, len(inp_text)):
# if key == inp_text[j]:
# counter += 1
# else:
# i += counter
# if counter == 1:
# result.append((key, 1))
# else:
# result.append((key, counter))
# break
# result.append((inp_text[-1], 1))
# return result

# def Unpack (inp_list):
# result=''
# for i in inp_list:
# result = result + i[0]*i[1]
# return result

# a = Squash(text)
# print(a)
# print (Unpack(a))

# *******************************от Сергея

# def coding(txt):
# count = 1
# res = ''
# for i in range(len(txt)-1):
# if txt[i] == txt[i+1]:
# count += 1
# else:
# res = res + str(count) + txt[i]
# count = 1
# if count > 1 or (txt[len(txt)-2] != txt[-1]):
# res = res + str(count) + txt[-1]
# return res

# def decoding(txt):
# num = ''
# res = ''
# for i in range(len(txt)):
# if not txt[i].isalpha():
# num += txt[i]
# else:
# res = res + txt[i] * int(num)
# num = ''
# return res








