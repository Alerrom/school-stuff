a = input()
b = []
k = 1
i = 0
while i < len(a)-1:
    b.append(a[i])
    while i < len(a)-1 and a[i] == a[i+1]:
        k += 1
        i += 1
    b.append(k)
    k = 1
    i += 1
if a[len(a)-2] != a[len(a)-1]:
    b.append(a[len(a)-1])
    b.append(1)
print(*b, sep = '')
