# 11399

N = int(input())

P = []
a = input().split()
for i in range(N):
    P.append(int(a[i]))

P.sort()
minTime = 0
for i in range(N):
    minTime += (N-i) * P[i]

print(minTime)