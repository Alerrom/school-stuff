s = input().split()
ch = input()
a = []
k = 0
for i in s:
    if ch == i:
        a.append(k)
    k += 1
if len(a) == 0:
    print('Отсутствует')
else:
    print(*a)
