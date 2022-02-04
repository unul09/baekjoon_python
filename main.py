# 1946
# 서류1등보다 면접등수가 같거나높은놈들 + 면접1등보다 서류등수가 같거나높은놈들 -> 둘의 교집합 XXXX
# 위 방법으로 몇번 시도해봤는데 안됨.
# 서류순으로 오름차순정렬, latest 합격자에 대하여

#https://suhwanc.tistory.com/118 이새끼 미친새끼임... 사고의 흐름이 매우 체계적..!
import sys

T = int(input())
for i in range(T):
    data = []
    N = int(input())
    for j in range(N):
        data.append(list(map(int, sys.stdin.readline().split())))

    if len(data) == 1:
        print(1)
        continue

    data.sort()
    cnt = 1
    latestOk = data[0][1]
    for j in range(1, len(data)):
        if data[j][1] < latestOk:
            cnt += 1
            latestOk = data[j][1]

    print(cnt)





