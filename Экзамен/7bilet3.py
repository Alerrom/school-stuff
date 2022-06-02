n = input()
a = []
for i in range(0, len(n)):
    a.append(n[i])
a.sort()
print(*a, sep = '')
a.sort(reverse = True)
print(*a, sep = '')
