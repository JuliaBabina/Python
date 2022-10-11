# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# Решение:

# tex = input('Введите текст, состоящий из слов, разделенных пробелами: ')
# del_let = "абв"
# spisok = [l for l in tex.split() if del_let not in l]
# print(' '.join(spisok))



# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# Решение:

# from random import randint

# def condition(p_name):
#     n = int(input(f'{p_name}, введите количество конфет, которое возьмете от 1 до 28: '))
#     while n < 1 or n > 28:
#         n = int(input(f'{p_name}, введите корректное количество конфет: '))
#     return n


# def p_print(p_name, n, left, value):
#     print(f"Ходил {p_name}, он взял {n}, теперь у него {left}. Осталось на столе {value} конфет.")

# player_1 = input("Введите имя первого игрока: ")
# player_2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2)
# if flag:
#     print(f"Первый ходит {player_1}")
# else:
#     print(f"Первый ходит {player_2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         k = condition(player_1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player_1, k, counter1, value)
#     else:
#         k = condition(player_2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player_2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player_1}")
# else:
#     print(f"Выиграл {player_2}")



# 3. Создайте программу для игры в ""Крестики-нолики"".

# Решение:

# import os
# os.system("cls")

# print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

# board = list(range(1,10))

# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)

# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "Вы выиграли!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)

# input("Нажмите Enter для выхода!")



# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Решение:

# def compression(data):
#     count = 1
#     res = ''
#     for i in range(len(data)-1):
#         if data[i] == data[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + data[i]
#             count = 1
#     if count > 1 or (data[len(data)-2] != data[-1]):
#         res = res + str(count) + data[-1]
#     return res

# def recovery(data):
#     number = ''
#     res = ''
#     for i in range(len(data)):
#         if not data[i].isalpha():
#             number += data[i]
#         else:
#             res = res + data[i] * int(number)
#             number = ''
#     return res


# some_data = input("Введите данные: ")
# print(compression(some_data))
# print(recovery(compression(some_data)))


