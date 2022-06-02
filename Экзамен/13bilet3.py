def sumdec(q):
    s = 0
    while q > 0:
        s += q%10
        q //= 10
    return s
def sumoct(x):
    s = 0
    q = oct(x)
    for i in q:
        if i in '01234567':
            s += int(i)
    return s
a = list(map(int, input().split()))
k = 0
for i in a:
    if sumdec(i) == sumoct(i):
        k += 1
        print(i)
print(k)
