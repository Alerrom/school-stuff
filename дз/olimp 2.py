a = list(map(int, input().split()))
print((1+a[0])*len(a)//2-sum(a[1::]))
