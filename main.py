# 1439
import math

S = input()

lastS = S[0]
cnt = 0
for i in range(1, len(S)):
    currentS = S[i]
    if lastS != currentS:
        cnt += 1
    lastS = currentS

cnt = int(math.ceil(cnt / 2))

print(cnt)

