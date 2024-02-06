lst = []
lst_r = []
res = []
with open('players.csv', 'r', encoding='utf-8') as fp:
    s = fp.readlines()
    for i in s:
        lst.append(i.split(';'))
    print(lst)
    for j in lst[1:]:
        lst_r.append([j[0]] + [int(j[1])] + [int(j[2][:-2])])
    print(lst_r)
    res = sorted(lst_r, key = lambda x: (-x[1], -x[2]))
    print(res)

    with open('results.csv', 'w', encoding='utf-8') as fr:
        fr.write('Спортсмен;место\n')
        fr.write(res[0][0] + ';1\n')
        for k in range(1, len(lst_r)):
            if res[k][1] == res[k-1][1] and res[k][2] == res[k-1][2]:
                fr.write(res[k][0] +';' + str(k) + '\n')
            else:
                fr.write(res[k][0] + ';' + str(k+1) + '\n')
