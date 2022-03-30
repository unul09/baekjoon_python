# 10989
import sys

num_counts = [0 for i in range(10001)]

N = int(sys.stdin.readline())
for _ in range(N):
    num_counts[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_counts[i] == 0:
        continue
    else:
        for j in range(num_counts[i]):
            print(i)
