# 1436

N = int(input())

cnt = 0
i = 666

while True:
    if '666' in str(i):
        cnt += 1
    if cnt == N:
        print(i)
        exit()
    else:
        i += 1