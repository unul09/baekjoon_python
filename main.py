# 1049

# (필요개수/6 올림) X 세트최저가,
# (필요개수/6 내림) X 세트최저가 + 나머지개수 X 단일최저가,
# 필요개수 X 단일최저가 비교, 작은값 출력

N, M = map(int, input().split())
price = [list(map(int, input().split())) for _ in range(M)]

setmin = price[0][0]
for i in range(M):
    if price[i][0] < setmin:
        setmin = price[i][0]

onemin = price[0][1]
for i in range(M):
    if price[i][1] < onemin:
        onemin = price[i][1]

import math
a = math.ceil(N / 6) * setmin
b = math.floor(N / 6) * setmin + (N % 6) * onemin
c = onemin * N

print(min(a, b, c))




