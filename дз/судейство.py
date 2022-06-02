def res(a):
    return (sum(a) - min(a) - max(a))/3
g = list(map(int, input().split()))
print(min(g), max(g))
print(res(g))
