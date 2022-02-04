# 2217

import sys
data = []
N = int(sys.stdin.readline())
for i in range(N):
    data.append(int(sys.stdin.readline()))

data.sort()
max = len(data) * data[0]
for i in range(N):
    if data[i] * (N - i) > max:
        max = data[i] * (N - i)

print(max)