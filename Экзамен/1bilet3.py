def prost(a):
    if a == 1 or i <= 0:
        return False
    k = 0
    x = 2
    while x < a**0.5 + 1:
        if a % x == 0:
            k += 1
        x += 1
    if k == 0:
        return True
    else:
        return False
m = 0
s = list(map(int,input().split()))
for i in s:
    if prost(i):
        m += 1
print(m)
