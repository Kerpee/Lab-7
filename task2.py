import numpy as np
import matplotlib.pyplot as plt

arr = np.genfromtxt('data2.csv', delimiter='', dtype=None, encoding='utf-8')
arr1 = np.vstack(arr)
arr2 = []
data = []
for i in range(len(arr1)):
    arr2.append(str(arr1[i]).replace("'", '').split(";"))
for i in range(1, len(arr2)):
    arr2[i][0] = arr2[i][0].replace('[', '')
    if arr2[i][0] == '':
        arr2[i][0] = 0.0
    data.append(float(arr2[i][0]))

plt.figure(figsize=(10, 5))
plt.hist(data, bins=20)
plt.title('Гистограмма данных')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(data, bins=20, density=True)
plt.title('Нормализованная гистограмма данных')
plt.xlabel('Значения')
plt.ylabel('Плотность')
plt.show()

std_dev = np.std(data)
print(f'Среднеквадратичное отклонение данных: {std_dev}')
