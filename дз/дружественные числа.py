def friend(a):
    s = 1
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            s += i + a//i
    return s
x, y = map(int, input().split())
if friend(x) == y and x == friend(y):
    print('YES')
else:
    print('NO')
