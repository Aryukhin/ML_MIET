dic = {}
count_symb = 0
with open('article_rus.txt', 'r', encoding='utf-8') as fp:
    for i in range(ord('а'), ord('я') + 1):
        dic[chr(i)] = 0
    dic['ё'] = 0
    for i in range(ord('a'), ord('z') + 1):
        dic[chr(i)] = 0
    for line in fp:
        for letter in line.lower().strip():
            if letter.isalpha():
                count_symb += 1
                dic[letter] += 1
    for j in dic.keys():
        dic[j] /= count_symb

    with open('article_rus_solve.txt', 'w', encoding='utf-8') as fp_write:
        res = dict(sorted(dic.items(), key = lambda x: -x[1]))
        for key, value in res.items():
            fp_write.write(f'{key} : {value:.3f} \n')
