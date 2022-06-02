a = list(map(int, input().split()))
b = []
for i in range(0, len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            b.append(a[i])
if len(b) == 0:
    print()
else:
    print(*set(b))
