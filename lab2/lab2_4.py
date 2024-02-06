import os
import string
import random
os.mkdir('example')
for i in range(1000):
    letters = string.ascii_letters + string.digits
    rand = ''.join(random.sample(letters, 10))
    with open(f'example/{rand}', 'w', encoding='utf-8') as fp:
        fp.write(f'test')