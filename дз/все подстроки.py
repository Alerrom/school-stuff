def pod(a):
    k = 1
    s = ''
    while k <= len(a):
        for i in range(len(a)):
            if len(a[i:i+k]) == k:
                s += a[i:i+k]
                s += ' '
        k += 1
    return(s)
for i in range(int(input())):
    print(pod(input()))
