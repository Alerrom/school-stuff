s = list(map(int, input().split()))
p = []
for i in s:
    if i not in p and 9<abs(i)<100:
        p.append(i)
if len(p)==0:
    print('нет двузначных элементов')
else:
    print(sum(p)/len(p))
