a = list(map(int, input().split()))
count = 0
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            count += 1
print(count)
