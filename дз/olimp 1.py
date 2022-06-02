a = int(input())
b = int(input())
while a != b:
    if a % 2 == 0 and a>= b*2:
        print(':2')
        a //= 2
    else:
        print('-1')
        a -= 1

