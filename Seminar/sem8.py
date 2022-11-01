# text = list(map(str, input('Введите строку: ').split()))
# text = filter(lambda x: 'абв' not in x, text)

# for i in text:
#     print(i, end=' ')


# ************************************************************

# list= "абвдлодоьбабвджлвбав"
# print(list)
# lis=list.replace("абв","")
# print(lis)

# ************************************************************

# lis1 = [1.1,2.2,3.001,4.4]
# lis2 = [round(lis1[n] - round(lis1[n]),10) for n in range(0,len(lis1))]
# print('Задание 2: ', max(lis2)-min(lis2))

# ************************************************************

# numbers = [2, 3, 4, 5, 6, 7, 5]
# diff = list([a*b for a, b in zip(numbers, numbers[:(len(numbers)//2) - 1: -1])])
# print(diff)

# ************************************************************






# Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы

# view model controller main
# работа с файлами csv и json

# def show_menu() -> int:
# print("\n" + "=" * 20)
# print("Выберите необходимое действие")
# print("1. Найти сотрудника")
# print("2. Сделать выборку сотрудников по должности")
# print("3. Сделать выборку сотрудников по зарплате")
# print("4. Добавить сотрудника")
# print("5. Удалить сотрудника")
# print("6. Обновить данные сотрудника")
# print("7. Экспортировать данные в формате json")
# print("8. Экспортировать данные в формате cmv")
# print("9. Закончить работу")
# return int(input("Введите номер необходимого действия: "))

import csv
import json
from pathlib import Path

# чтение и запись csv и json файлов:

# def read_csv() -> list:
# employee = []
# with open(Path.cwd() / 'database.csv', 'r', encoding='utf-8') as fin:
# csv_reader = csv.reader(fin)
# for row in csv_reader:
# temp = {}
# temp["id"] = int(row[0])
# temp["last_name"] = row[1]
# temp["first_name"] = row[2]
# temp["position"] = row[3]
# temp["phone_number"] = row[4]
# temp["salary"] = float(row[5])
# employee.append(temp)
# return employee

# def read_json() -> list:
# employee = []
# with open(Path.cwd() / 'database02.json', 'r', encoding='utf-8') as fin:
# for line in fin:
# temp = json.loads(line.strip())
# employee.append(temp)
# return employee

# def write_csv(employees: list):
# with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8') as fout:
# csv_writer = csv.writer(fout)
# for employee in employees:
# csv_writer.writerow(employee.values())

# def write_json(employees: list):
# with open(Path.cwd() / 'database02.json', 'w', encoding='utf-8') as fout:
# for employee in employees:
# fout.write(json.dumps(employee) + '\n')

# обращение по ключу 

# for employee in employees:
# if employee['id'] == id:
# return employee


# выборка диапазон

# def find_employees_by_salary_range(employees: list) -> list:
# result = []
# lo, hi = get_salary_range()
# for employee in employees:
# if lo <= employee["salary"] <= hi:
# result.append(employee)
# return result

# искать так 

# for employee in employees:
# if employee['last_name'] == last_name:
# return employee

# пищем в контроллере
# employees = read_csv()

# работаем со списками, а не файлами, поэтому без разницы какой формат файла

# здесь csv главный, а json добавочный


