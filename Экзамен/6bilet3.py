def palin(s):
    if s == s[::-1] and s.isalpha():
        return True
    else:
        return False
a = list(map(str, input().split()))
k =0
p = []
for i in a:
    if palin(i):
        k += 1
        p.append(i)
if k == 0:
    print('нет таких слов')
elif k == 1:
    print(1)
else:
    for j in range(0, len(p)-1):
        for y in range(len(p)-1-j):
            if len(p[y])<len(p[y+1]):
                p[y+1], p[y] = p[y], p[y+1]
    print(k)
    print(*p, sep=', ')
    
