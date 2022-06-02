def prav(q):
    k = 0
    for i in range(len(q)-1):
        if int(q[i+1]) < int(q[i]):
            k += 1
    if k == 0:
        return True
    else:
        return False
a = input().split()
f = 0
for i in a:
    if prav(i):
        f += 1
if f == 0:
    print('нет таких чисел')
else:
    print(f)
