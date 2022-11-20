# Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.
import random as rn
length = 5

def Table(length): # создание таблицы
    print(f"Квадратная матрица {length}x{length}: ")
    examination = [[rn.randint(1, 10) for j in range(length)] for i in range(length)]
    [print(rows) for rows in examination]
    return examination
tab =[[]] * length
tab = Table(length)

def Summ(table): # Поиск суммы диагонали
    sum = 0
    for i in range(len(table)):
        for j in range(len(table)):
            if i==j:
                sum = sum + table[i][j]
    print(f"Сумма главной диагонали = {sum}")
    return sum

def Maximum(table): # сумма каждой строчки
    list_max = []
    for i in range(len(table)):  
        sum =0
        for j in range(len(table)):
            sum = sum + table[i][j]
        list_max.append(sum)
    print(f"\nСумма цифр в каждой строчке: {list_max}")
    return list_max

def Result(table,sum): # Сравнение сумм
    count = 0
    for i in range(len(table)):
        if table[i] > sum:
            print(f"Сумма элементов {i+1} строки превосходит сумму главной диагонали")
            count+=1
    if count == 0:
        print("Сумма главной диагонили больше суммы каждой строки")
Result(Maximum(tab),Summ(tab))


