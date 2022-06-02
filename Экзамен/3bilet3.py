def vzprost(x, y):
    while x>0 and y>0:
        if x>y:
            x %= y
        elif x == y:
            return False
        else:
            y %= x
    if x + y == 1:
        return True
    else:
        return False
a = list(map(int, input().split()))
p = 1
k = 0
for i in range(len(a)-1):
    for j in range(p, len(a)):
        if vzprost(a[i], a[j]):
            k += 1
    p += 1
print(k)
