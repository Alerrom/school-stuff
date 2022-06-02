def ist(x):
    a = str(x)
    if '3' in a:
        return True
    else:
        return False
s = list(map(int, input().split()))
for i in range(len(s)):
    p = max(s)
    if ist(p):
        break
    else:
        s[s.index(p)] = 0
print(p, s.index(p))
 
