n = int(input())
a = []
k = 1
s = 1
while len(a) < n:
    for i in range(s):
        a.append(k)
    if s == k:
        s += 1
    if k < s:
        k += 1
print(*a[:n])
