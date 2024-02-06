from random import randint
count = 0
ip_all = ''
with open('ip.log', 'w', encoding='utf-8') as fp:
    while (count < 10000):
        a = randint(0,255)
        b = randint(0,255)
        c = randint(0,255)
        d = randint(0,255)
        ip = str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d) + '\n'
        if ip not in ip_all:
            ip_all += ip
            count += 1
    fp.write(ip_all)

