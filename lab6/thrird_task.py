# 2 var
import numpy as np
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def matr(N):
    P = np.random.randint(-10, 10, N)
    Q = np.random.randint(-10, 10, N)

    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            r = 1 / (1 + (Q[j] - P[i]) ** 2)
            row.append(r)
        matrix.append(row)
    return matrix


if __name__ == "__main__":
    start = time.perf_counter()
    # Использование многопроцессорности

    # with ProcessPoolExecutor(max_workers=None) as executor:
    #     future = executor.submit(matr, 5000)
    #     result = future.result()


    # Базовый вызов

    # result = matr(5000)

    # Использование многопоточности

    with ThreadPoolExecutor(max_workers=None) as executor:
        future = executor.submit(matr, 5000)
        result = future.result()

    finish = time.perf_counter()

    print(f'The time is {finish - start}')

# Без использования многопроцессорности
# The time is 17.7919322


# С использованием многопроцессорности
# The time is 217.9143072


# С использованием многопоточности
# The time is 16.9122773
