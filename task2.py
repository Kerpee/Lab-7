import numpy as np
import matplotlib.pyplot as plt

arr = np.genfromtxt('data2.csv', delimiter='', dtype=None, encoding='utf-8')  # Получаем данные из таблицы
arr1 = np.vstack(arr)  # Разбиваем массив на массивы, которые определяются строчкой
arr2 = []
data = []
for i in range(len(arr1)):  # Убираем ' для более удобной обработки данных, также делим данные на более мелкие массивы
    arr2.append(str(arr1[i]).replace("'", '').split(";"))
for i in range(1, len(arr2)):
    arr2[i][0] = arr2[i][0].replace('[', '')  # Приводим данные для перевода в тип данных float
    if arr2[i][0] == '':  # Форматируем данные
        arr2[i][0] = 0.0
    data.append(float(arr2[i][0]))

plt.figure(figsize=(10, 5))
plt.hist(data, bins=20)  # Создаём гистограму
plt.title('Гистограмма данных')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(data, bins=20, density=True)  # Создаём нормализированную гистограму
plt.title('Нормализованная гистограмма данных')
plt.xlabel('Значения')
plt.ylabel('Плотность')
plt.show()

std_dev = np.std(data)
print(f'Среднеквадратичное отклонение данных: {std_dev}')
