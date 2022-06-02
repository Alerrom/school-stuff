a = list(map(int, input().split()))
count = 0
for i in range(0, len(a)-1):
    for j in range(i+1, len(a)):
        if a[j] < a[i]:
            a[i], a[j] = a[j], a[i]
            count += 1
print(count)
