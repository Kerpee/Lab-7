import numpy as np
from time import perf_counter
start_t = perf_counter()  # Начало отсчёта времени
arr1 = np.random.rand(1000000)
arr2 = np.random.rand(1000000)
res = np.multiply(arr1, arr2)
end_t = perf_counter()  # Окончание отсчта времени
time = end_t-start_t  # Подсчёт выполнение перемноения матриц
print(res, f'\nВремя выполнения в секундах:{time}')
