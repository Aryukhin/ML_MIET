import os
from threading import Thread
from time import time


def foo(root, file):
    if file.endswith('.txt'):
        with open(str(os.path.join(root, file))) as txt:
            if 'key' in txt.read():
                print(f"True: {os.path.join(root, file)}")
            else:
                print(f"False: {os.path.join(root, file)}")


start_time = time()
threads = []
for root, dirs, files in os.walk("d1"):
    for file in files:
        t = Thread(target=foo, args=(root, file))
        t.start()
        threads.append(t)

for t in threads:
    t.join()

time_one_thread = time() - start_time
print(f"--- {time_one_thread} seconds ---")

start_time = time()
threads = []
for root, dirs, files in os.walk("d1"):
    for file in files:
        foo(root, file)


time_one_thread = time() - start_time
print(f"--- {time_one_thread} seconds ---")