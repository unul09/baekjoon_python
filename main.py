# 2231

N = int(input())

if N < 20:
    min = 1
else:
    min = N - len(str(N)) * 9


for i in range(min, N + 1):
    result = i + sum(list(map(int, str(i))))

    if result == N:
        print(i)
        exit()

print(0)


