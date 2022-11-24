#В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
#Каждому месяцу соответствует своя строка.
#Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты. 
import random 
from datetime import datetime, timedelta

temperature = [0] * 5
value_sum=0
value = []
weekly_maximum = 0
weekly_minimum = 1000
count = 0
month = ['May','June','July','August','September']
temperature[0] = [random.randint(9,21) for i in range(31)]
temperature[1] = [random.randint(18,31) for i in range(30)]
temperature[2] = [random.randint(17,30) for i in range(31)]
temperature[3] = [random.randint(18,31) for i in range(31)]
temperature[4] = [random.randint(8,16) for i in range(30)]
for row in temperature:
    print(month[count], row)
    count+=1
for i in range(len(temperature)):
    for j in range(len(temperature[i])):
        value.append(temperature[i][j])
for i in range(len(value) - 6):
    value_sum = 0
    value_sum = value[i] + value[i+1] + value[i+2] + value[i+3] + value[i+4] + value[i+5] + value[i+6]
    if value_sum > weekly_maximum:
        weekly_maximum = i
    elif value_sum < weekly_minimum:
        weekly_minimum = i
start = '2022-05-01'
dt = datetime.strptime( start, '%Y-%m-%d')
start_max_day = (dt + timedelta(days=weekly_maximum)).strftime('%Y-%m-%d')
finish_max_day = (dt + timedelta(days=weekly_maximum+7)).strftime('%Y-%m-%d')
start_min_day = (dt + timedelta(days=weekly_minimum)).strftime('%Y-%m-%d')
finish_min_day = (dt + timedelta(days=weekly_minimum+7)).strftime('%Y-%m-%d')
print(f"Самый жаркий 7-дневный промежуток с {start_max_day} по {finish_max_day}")
print(f"Самый холодный 7-дневный промежуток с {start_min_day} по {finish_min_day}")