import threading
import time

resourses = 0

semaphor = threading.Semaphore(1)
#semaphor = threading.Semaphore(2)
#semaphor = threading.Semaphore(3)

def foo():
    global resourses
    with semaphor:
        resourses += 1
        print(f"\n Thread {threading.current_thread().name} увеличил общий ресурс: {resourses}")
        time.sleep(1)
        print(f'-------------')
        time.sleep(1)

threads = []
for i in range(10):
    thread = threading.Thread(target=foo)
    threads.append(thread)
    thread.start()

for t in threads:
    t.join()

print(f'{resourses}')

