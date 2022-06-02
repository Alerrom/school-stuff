def palin(x):
    if x == x[::-1]:
        return True
    else:
        return False
a = input()
f = '0123456789'
s = []
k = 0
p = []
for i in a:
    if i in f:
        s.append(i)
    else:
        if palin(s) and len(s) != 0:
            k += 1
            p.append(s)
        s = []
if palin(s) and len(s) != 0:
            k += 1
            p.append(s)
p.sort()
print(k)
for i in p:
    print(*i, sep ='')
