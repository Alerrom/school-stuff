def anag(x, y):
    if len(x) == len(y) and len(set(x)) == len(set(y)):
        a = set(x)
        for el in a:
            if x.count(el) != y.count(el):
                return False
        return True
    return False
a = []
s = ''
for i in range(int(input())):
    a.append(input().lower())
for i in range(len(a)-1):
    s += a[i]
    for j in range(i+1, len(a)-1):
        if anag(a[i], a[j]) and a[j] != '':
            s += ' ' + a[j]
            a.pop(j)
    print(s)
    s = ''
