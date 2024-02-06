mask = input().split('.')
ans = ''
with open('ip.log', 'r', encoding='utf-8') as fp:
    with open('ip_solve.log', 'w', encoding='utf-8') as fpw:
        for line in fp:
            x = line.split('.')
            for i in range(4):
                c = int(x[i]) & int(mask[i])
                ans += str(c) + '.'
            fpw.write(ans[:-1] + '\n')
            ans = ''