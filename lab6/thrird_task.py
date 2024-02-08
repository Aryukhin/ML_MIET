# 2 var
import numpy as np
import time
from concurrent.futures import ProcessPoolExecutor


start = time.perf_counter()

P = np.random.randint(-10, 10, 5000)
Q = np.random.randint(-10, 10, 5000)


def matr(N):
    x = []
    matrix = []
    for i in range(N):
        for j in range(N):
            r = 1 / (1 + (Q[j] - P[i]) ** 2)
            x.append(r)

        matrix.append(x)
        x = []


# matix = matr(5000)

with ProcessPoolExecutor(max_workers=None) as executor:
    # Запуск задачи параллельно
    future = executor.submit(matr, 5000)
    # Ожидание результата и получение его
    # result = future.result()

finish = time.perf_counter()

print(f'The time is {finish - start}')

# The time is 26.6003019
