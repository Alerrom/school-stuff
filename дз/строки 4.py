a = input()
ch = 0
for i in range(len(a)):
    if a[i] == 'g' or a[i] == 'c':
        ch += 1
print(float(ch/len(a)*100))
