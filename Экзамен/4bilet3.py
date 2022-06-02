a = list(map(str, input().split()))
dlin = 0
for i in a:
    if i[0] in 'Aa':
        if dlin == 0 or len(i) > dlin:
            dlin = len(i)
for i in a:
    if i[0] in 'Aa':
        if len(i) < dlin:
            dlin = len(i)
p = []
k = 0
for i in a:
    if i[0] in 'Aa' and len(i) == dlin:
        k += 1
        p.append(i)
p.sort()
if k == 0:
    print('нет таких слов')
else:
    print(k)
    print(*p, sep =', ')
