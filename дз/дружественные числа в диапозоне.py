def friend(a):
    s = 1
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            s += i + a//i
    return s

a, b = map(int, input().split())
e = []
for i in range(a, b + 1):
    if i == friend(friend(i)) and friend(i) in range(a, b+1) and i not in e:
        e.append(i)
        e.append(friend(i))
if len(e) == 0:
    print(0)
else:
    for i in range(0, len(e), 2):
        print('({},{})'.format(e[i], e[i+1]))
