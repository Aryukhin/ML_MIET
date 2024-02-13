from pathlib import Path
import time
from concurrent.futures import ProcessPoolExecutor

# def f(word):
#     top_lvl = Path.cwd().rglob(f'*.txt')
#     res = []
#     for file_path in top_lvl:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             if word in file.read():
#                 res.append(file_path.name)
#     return res
#
#
#
#
# #f1 = f(word='key')
#
# if __name__ == "__main__":
#     word_to_search = 'key'
#
#     start = time.perf_counter()
#
#     # Используем ThreadPoolExecutor для выполнения функции параллельно
#     with ProcessPoolExecutor(max_workers=None) as executor:
#         # Запускаем выполнение функции search_files_with_keyword(word) с аргументом word_to_search
#         result = executor.submit(f, word_to_search)
#         # Получаем результат выполнения функции
#         found_files = result.result()
#
#     #found_files = f(word_to_search)
#
#     finish = time.perf_counter()
#
# print(f'Найденные файлы: {found_files}')
# print(f'Время выполнения: {finish - start} секунд')
#
# # Без многопоточности
#
# # Найденные файлы: ['1.txt', '2.txt', '1.txt', '3.txt', '5.txt', '2.txt', '4.txt', 'LICENSE.txt', 'entry_points.txt']
# # Время выполнения: 0.10076260000000001 секунд
#
#
# # С многопоточностью
#
# # Найденные файлы: ['1.txt', '2.txt', '1.txt', '3.txt', '5.txt', '2.txt', '4.txt', 'LICENSE.txt', 'entry_points.txt']
# # Время выполнения: 0.09788229999999999 секунд


from pathlib import Path
import time
from concurrent.futures import ProcessPoolExecutor


def f(file_path, word):
    with open(file_path, 'r', encoding='utf-8') as file:
        if word in file.read():
            return file_path.name
    return None


if __name__ == "__main__":
    word_to_search = 'key'
    start = time.perf_counter()
    top_lvl = list(Path.cwd().rglob('*.txt'))

    found_files = []

    # Используем ProcessPoolExecutor для параллельной обработки файлов
    with ProcessPoolExecutor(max_workers=None) as executor:
        # Запускаем выполнение функции f для каждого файла в пуле процессов
        results = [executor.submit(f, file_path, word_to_search) for file_path in top_lvl]

        # Получаем результаты выполнения функций
        for result in results:
            if result.result():
                found_files.append(result.result())

    finish = time.perf_counter()

    print(f'Найденные файлы: {found_files}')
    print(f'Время выполнения: {finish - start} секунд')

# С использование многопроцессорности

# Найденные файлы: ['1.txt', '2.txt', '1.txt', '3.txt', '5.txt', '2.txt', '4.txt', 'LICENSE.txt', 'entry_points.txt']
# Время выполнения: 0.4241788 секунд
