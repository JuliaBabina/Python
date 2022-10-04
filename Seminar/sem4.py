# 1. Больше предыдущего

# На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел. 
# Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа, 
# то есть, стоят вслед за меньшим числом. 

# Формат входных данных
# На вход программе подается строка текста из разделенных пробелами натуральных чисел.

# Формат выходных данных
# Программа должна вывести одно число – количество элементов списка, больших предыдущего.

# Тестовые данные 🟢
# Sample Input 1:
# 1 2 3 4 5
# Sample Output 1:
# 4
# Sample Input 2:
# 1 1 3 2 2 1 1 1 1
# Sample Output 2:
# 1
# Sample Input 3:
# 5 4 3 2 1
# Sample Output 3:
# 0


# Наше недоделанное
# string = input ('Введите строку: ')
# lst = []
# for i in range(len(string)):
#     lst.append(string[i])
# print(lst)

# if lst[i] == " ":
#     del lst[i]

# print(lst)

#******************************************************

# number_str = input ('Введите строку: ')
# spisok = []
# for i in number_str:
#     try:
#         i = int(i)
#         spisok.append(i)
#     except:
#         continue

# count = 0
# max = spisok[0]
# for i in spisok:
#     if i > max:
#         max = i
#         count += 1
    
# print(f"Количество чисел соответствующих условию: {count}")

#******************************************************

# numbs = list(map(int, input('  input:').split()))
# count = 0
# for i in range(1,len(numbs)):
#     if numbs[i-1] < numbs[i]:
#         count += 1

# print(count)

# 2. Транслит (вводим строку на русском, а он ее транслитом выдает)
# 'a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o',
#  'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya'

# из интернетов

# dic = {'Ь':'', 'ь':'', 'Ъ':'', 'ъ':'', 'А':'A', 'а':'a', 'Б':'B', 'б':'b', 'В':'V', 'в':'v',
#        'Г':'G', 'г':'g', 'Д':'D', 'д':'d', 'Е':'E', 'е':'e', 'Ё':'E', 'ё':'e', 'Ж':'Zh', 'ж':'zh',
#        'З':'Z', 'з':'z', 'И':'I', 'и':'i', 'Й':'I', 'й':'i', 'К':'K', 'к':'k', 'Л':'L', 'л':'l',
#        'М':'M', 'м':'m', 'Н':'N', 'н':'n', 'О':'O', 'о':'o', 'П':'P', 'п':'p', 'Р':'R', 'р':'r', 
#        'С':'S', 'с':'s', 'Т':'T', 'т':'t', 'У':'U', 'у':'u', 'Ф':'F', 'ф':'f', 'Х':'Kh', 'х':'kh',
#        'Ц':'Tc', 'ц':'tc', 'Ч':'Ch', 'ч':'ch', 'Ш':'Sh', 'ш':'sh', 'Щ':'Shch', 'щ':'shch', 'Ы':'Y',
#        'ы':'y', 'Э':'E', 'э':'e', 'Ю':'Iu', 'ю':'iu', 'Я':'Ia', 'я':'ia'}
       
# alphabet = ['Ь', 'ь', 'Ъ', 'ъ', 'А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё',
#             'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о',
#             'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч',
#             'Ш', 'ш', 'Щ', 'щ', 'Ы', 'ы', 'Э', 'э', 'Ю', 'ю', 'Я', 'я']
 
# print("Enter text: ")
# st = str(input())
# result = str()
 
# len_st = len(st)
# for i in range(0,len_st):
#     if st[i] in alphabet:
#         simb = dic[st[i]]
#     else:
#         simb = st[i]
#     result = result + simb
 
# print(result)

#*************************************************************

# Проверка ДЗ2.1
# numb = float(input())
# summ = 0
# for el in str(numb):
#     if el != '.':
#         summ += int(el)
# print(summ)

#*************************************************************

# s = '0.56'
# summ = 0
# for i in s:
#     if i.isdigit():
#         summ += int(i)
# print(summ)

#*************************************************************

# n = float(input('Введите число - '))
# while n % 1 > 0:
#     n *= 10
# summ = 0
# while n > 0:
#     summ += n % 10
#     n //= 10
# print(int(summ))

#*************************************************************

# num = input()
# res = 0
# for digit in num:
#     if digit.isdigit():
#       res += int(digit)  
# print("Сумма:", res)

#*************************************************************

# import random
# list = [random.randint(0,10) for i in range(random.randint(3,10))]
# print(f"Заданный список:\n{list}")
# sumOdd = 0
# i = 1
# while(i<len(list)):
#     sumOdd = sumOdd + list[i]
#     i=i+2
# print(f"Cумму элементов списка, стоящих на нечётной позиции = {sumOdd}")

#*************************************************************

# def sum_nums(num):
#     sum = 0
#     for i in str(num):
#         if i != ".":
#             sum += int(i)
#     return sum

#*************************************************************

# N = input("Введите число: ")
# sum = 0
# for i in N:
#     if i != "." and i != ",":
#         sum = sum + int(i)
# print(sum)

#*************************************************************


#2.2

# number = int(input("Введите число: "))
# product = 1
# arr = []

# for i in range(1, number+1):
#     product *= i
#     arr.append(product)
# print(arr)

#*************************************************************

# def Factorial (number):
#     if (number == 1):
#         return 1
#     else:
#         return number*Factorial(number-1)

# n=int(input('Введите число: '))
# fact_list = []
# for i in range (1,n+1):
#     fact_list.append(Factorial(i))
# print(fact_list)


# 2.3

# num = int(input("Введите число: "))
# dic = {}
# sum = 0

# for i in range(1, num+1):
#     dic[i] = round((1+1/i)**i)
#     sum += dic[i]
# print(f'{dic} -> {sum}')


# 2.4

# numN = int(input('Введите число N: '))
# list = []
# for i in range(-numN,numN+1):
#     list.append(i)
# print(list)
# position1 = int(input('Укажите первую позицию цифры из списка, которую нужно перемножить: '))
# position2 = int(input('Укажите вторую позицию цифры из списка, которую нужно перемножить: '))
# print(f'Произведение чисел = {list[(position1-1)]*list[(position2-1)]}')

# #*************************************************************

# from pdb import line_prefix


# n = int(input('Введите число: '))
# numbers = list(range(-n,n+1))
# sum=0
# pos = []
# file='C:\\Users\\МSI\\Desktop\\Python for n00bz\\seminars\\sem2\\HW\\positions.txt'
# with open(file,'r') as data:
#     for line in data:
#         pos.append(int(line))
#     print (numbers, '\n', pos)
#     for i in range(len(pos)):
#         index=pos[i]
#         sum+=numbers[index]
#     print (sum)

# #*************************************************************

# input = int(input(" Input N: "))

# array = []

# for i in range(input*-1,input+1):
#     array.append(i)

# with open ('file.txt') as data:
#     op = 1
#     for line in data.readlines():
#         pos = line
#         op = array[int(pos)] * op
#     print(array, " = ", op)

# #*************************************************************

# import random
# n=int(input('input number '))
# list=[]
# for i in range(n):                      # генератор случайных чисел
#     a=random.randint(-n, n)
#     list.append(a)   
# print (list)
# index_list = input(f'введите позиции элементов от 1 до {n} через пробел').split()
# result=1
# for j in range(len(index_list)):        # перебор элементов с номерами позиций
#     a=int(index_list[j])-1
#     print (f'{result}*{int(list[a])}', end=' ')
#     result*=int(list[a])    
# print (f'= {result}')

#*************************************************************

# N = int(input("Введите число: "))
# elements = list(range(-N, N+1))
# print(elements)
# result = 1
# pos = open('file.txt', 'r')
# for i in pos:
#     print(i)
#     result *= elements[int(i)]
# pos.close()
# print(result)

#*************************************************************

# n = int(input("Введите число: "))
# pos_a = int(input(f"Укажите позицию числа A от 1 до {n * 2 + 1}: "))
# pos_b = int(input(f"Укажите позицию числа B от 1 до {n * 2 + 1}: "))
# range_n = list(range(-n, n + 1))
    
# a = range_n[pos_a-1]
# b = range_n[pos_b-1]
# print(f'{a} * {b} = {a * b}')

#*************************************************************

# 2.5. Перемешивает список
# Реализуйте алгоритм перемешивания списка. num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# import random

# # arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_arr = []
# random_num = None

# while len(new_arr) < len(arr):
#     random_num = arr[random.randint(0, len(arr))-1]
#     if not random_num in new_arr:
#         new_arr.append(random_num)
# print(new_arr)

#*************************************************************

# list = ["Anna", "Alex", 3.14159, 0]
# for i in range(len(list)):
#     index_a = random.randint(0, len(list) - 1)
#     list[i], list[index_a]=list[index_a],list[i]

#*************************************************************

# import random 
# y = ['Apple', '2 ', '-5675 ', '0.678 ', 'morning']
# random.shuffle(y)
# print(y)



# from random import randint

# my_list = [1, 3, 44, 55, 21, 5]

# for i in range(len(my_list)):
#     r = randint(0,i)
#     temp = my_list[r]
#     my_list[r] = my_list[i]
#     my_list[i] = temp

# print(my_list)

#*************************************************************

# import random
# list = [random.randint(0,10) for i in range(random.randint(5,20))]
# print(f"Исходный список:\n{list}")
# def mix_list(list_original):
#     list = list_original[:]
#     list_length = len(list)
#     for i in range(list_length):
#         index_aleatory = random.randint(0, list_length - 1)
#         temp = list[i]
#         list[i] = list[index_aleatory]
#         list[index_aleatory] = temp
#     return list
# mixed_list = mix_list(list)
# print("Перемешанный список: ")
# print(mixed_list)



# transleterate = \
#   {'а': 'a','б': 'b','в': 'v','г' : 'g','д' : 'd','е' : 'e','ж' : 'zh','з' : 'z','и' : 'i',
#   'й' : 'y','к' : 'k','л' : 'l','м' : 'm','н' : 'n','о' :'o','п' : 'p','р' : 'r','с' : 's',
#   'т' : 't','у' : 'u','ф' : 'f','х' : 'kh','ц' : 'ts','ч' : 'ch','ш' : 'sh','щ' : 'shch',
#   'ь' : '\'','ы' :'y','ъ' : '','э' : 'e','ю' : 'yu','я' : 'ya'}
# text = input('input: ')

# for i in text:
#     print(transleterate[i], end = "")

#*************************************************************


# aplphabetE = \
# ['a', 'b', 'v', 'g', 'd', 'e', 'yo', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p','r', 
# 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '\'', 'e', 'yu', 'ya']

# aplphabetR = \
# ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 
# 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

# base = input('Введите слово: ')
# word=[]

# for i in range(len(base)):
#     word.append(aplphabetR.index(base[i]))
#     index = word[i]
#     print(aplphabetE[index], end='')

#*************************************************************

# for i in range(len(base)):
#     print(base[i].replace(aplphR[aplphR.index(base[i])],aplphE[aplphR.index(base[i])]), end = '')

#*************************************************************

# от Сергея

# t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

# start_index = ord('а')
# title = 'Переводим этот текст, сейчас!'
# print(title.lower())

# slug = ""
# for s in title.lower():

# 	if "а" <= s <= "я":
# 		slug += t[ord(s) - ord('а')]
	
# 	else:
# 		slug += s



# print(slug)







