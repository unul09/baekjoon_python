# 16953

a, b = map(int, input().split())

cnt = 1

while True:

    if a == b:
        break

    if a > b:
        print(-1)
        exit()

    if b%2 == 0:
        b = int(b/2)
        cnt += 1
    elif b%10 == 1:
        b = int(b/10)
        cnt += 1
    else:
        print(-1)
        exit()

print(cnt)





