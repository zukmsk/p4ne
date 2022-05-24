#Импорт фукций
from openpyxl import load_workbook
from matplotlib import pyplot
#Загружаем WB
wb = load_workbook('data_analysis_lab.xlsx')
#Загружаем столбцы
sheet = wb['Data']
#Задаем функцию получения значений
def getvalue(x): return x.value
#Получаем только значения
list_x = list(map(getvalue, sheet['A'][1:]))
list_y1 = list(map(getvalue, sheet['D'][1:]))
list_y2 = list(map(getvalue, sheet['C'][1:]))
#Рисуем графики
pyplot.plot(list_x, list_y1, label='Temp')
pyplot.plot(list_x, list_y2, label='Act')
#Смотрим График
pyplot.show()