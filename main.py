# 1449
# 테이프 길이만큼의
import sys
N, L = map(int, sys.stdin.readline().split())
leak = list(map(int, sys.stdin.readline().split()))
leak.sort()

temp = leak[0]
cnt = 1 # 물새는곳은 무조건 1개이상이므로 처음부터 테이프 할당

for i in range(1, N):
    if leak[i] - temp < L:
        continue
    else:
        temp = leak[i] # 새로운 테이프
        cnt += 1

print(cnt)