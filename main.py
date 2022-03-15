# 1002
import math

T = int(input())

for _ in range(0, T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    ans = 0
    dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if r2 > r1: r2, r1 = r1, r2

    if dis == 0 and r1 == r2:
        ans = -1
    elif dis == r1+r2 or dis == abs(r1-r2):
        ans = 1
    elif abs(r1-r2) < dis < (r1+r2): # 이 조건에서 계속 틀린듯. 조건 명확히 설정할것
        ans = 2
    else:
        ans = 0

    print(ans)