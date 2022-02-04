# 1789
# 1+...n < S < 1+...n+1 일때 n 구하기


S = int(input())
N = 1

while True:
    if S < (N+1)*(N+2)/2:
        break
    N += 1

print(N)


