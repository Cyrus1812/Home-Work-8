# В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу.
#  Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.
import random as rn

def table():
    group = 10
    examination = [[rn.randint(2, 5) for j in range(rn.randint(20,30))] for i in range(group)]
    [print(rows) for rows in examination]
    return examination

def average(examination):
    average_value =[]
    for i in range(len(examination)):
        sum =0
        for j in range(len(examination[i])):
            sum = sum + examination[i][j]
        average_number = sum / len(examination[i])
        average_value.append(round(average_number,2))
    print(average_value)
    return average_value

def best_group(average_value):
    max = 0
    for i in range(len(average_value)):
        if average_value[i] > max:
            max = average_value[i]
            index = i+1
    print(f"Группа с наилучшим средним баллом {index} - {max}")
    
best_group(average(table()))








