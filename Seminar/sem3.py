# Из 1 ДЗ про предикаты

# for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 print(not (x or y or z) == (not x and not y and not z))

#****************************************************************************************


# 1. Орел и решка

# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, 
# а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.

# Примечание. Если выпавших Решек нет, то необходимо вывести число 
# 0
# 0.

# Тестовые данные 🟢
# Sample Input 1:
# ОРРОРОРООРРРО
# Sample Output 1:
# 3
# Sample Input 2:
# ООООООРРРОРОРРРРРРР
# Sample Output 2:
# 7
# Sample Input 3:
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
# Sample Output 3:
# 31

# Решение

# string = input('Введите строку: ')
# t=0
# while "Р"*(t+1) in string:
#     t+=1
    
# print(t)



#***********************************************

# stroka = input('Введите строку: ').split('О')
# res = max(stroka, key=len)
# print(len(res))

#***********************************************

# text = input("Введите произвольную последовательность букв О и Р: ")
# count = 0
# max_count = 0

# for char in text:
#     if char == "Р":
#         count += 1
#     else:
#         count = 0
#     if max_count < count:
#         max_count = count
# print(max_count)

#***********************************************

# n = input()
# total = 0
# max = 0
# for i in n:
#     if i == 'Р':
#         total += 1
#         if total > max:
#             max = total
#     else:
#         if total > max:
#             max = total
        
#         total = 0
# print(max)

#***********************************************

# n = input("Введите результат выпадения Орла и решки:")
# total = 0
# max = 0
# for i in n:
#     if i == 'Р':
#         total += 1
#         if total > max:
#             max = total
#     else:
#         if total > max:
#             max = total
#         total = 0
# print(max)

#***********************************************От Сергея

# s=input()
# t=0
# while "Р"*(t+1) in s:
#     t+=1
# if t!=0:
#     print(t)
# else:
#     print(0)

#***********************************************


# 2. Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. 
# Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.

# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" 
# (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, 
# нумерация начинается с единицы

# Формат входных данных
# В первой строке подаётся число 
# n
# n – количество холодильников. В последующих 
# n
# n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 
# 5
# 5 до 
# 100
# 100 символов.

# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.

# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
# 1 2 3
# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8

# Начало, доделать

n=int(input('Введите количество холодильников: '))
f=[]
hacker =  ['a', 'n', 't', 'o', 'n','']
count=0
otvet=[]
for i in range(1,n+1):
    f = list(input(f'Введите код {i} холодильника: '))   
    for j in hacker:
        for k in f:
          if hacker[j]==f[k]:
            count+=1
            otvet.append(count)
print(otvet)

    






# 3. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# strings = ["1", "another string", "string 3", "hello world", "123"]

# num_to_search = input("Введите число для поиска: ")
# found = False

# for s in strings:
#     if num_to_search in s:
#         found = True
#         break
# if found:

#     print("Число найдено")
# else:
#     print("Число не найдено")

#****************************************************************

# inputList = ['asdla;slkd', '42', 'asdasd', '0']
# print(any(map(lambda x: str(x).isdigit(), inputList)))

#****************************************************************

# list = input('Введите список через пробел: ').split(" ")
# num = input('Введите число: ')

# for i in list:
#     if i == num:
#         print("YES")

#****************************************************************

# array = ['osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen', 'anton', 'aoooooooooontooooo', 'elelelelelelelelelel', 'ntoneeee', 'tonee', '253235235a5323352n25235352t253523523235oo235523523523n', 'antoooooooooooooooooooooooooooooooooooooooooooooooooooon', 'unton']
# number = 252
# for word in array:
#     if str(number) in word:
#         print(True)
#     else:
#         print(False)



