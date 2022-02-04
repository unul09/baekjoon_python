# 1946
# 서류1등보다 면접등수가 같거나높은놈들 + 면접1등보다 서류등수가 같거나높은놈들 -> 둘의 교집합
import sys

T = int(input())
for i in range(T):
    data = []
    N = int(input())
    for j in range(N):
        data.append(list(map(int, sys.stdin.readline().split())))

    temp1 = []
    temp2 = []
    data.sort(key=lambda x: x[1])
    for j in range(len(data)):
        if data[j][0] == 1:
            temp1 = data[:j+1]

    data.sort()
    for j in range(len(data)):
        if data[j][1] == 1:
            temp2 = data[:j+1]

    for k in range(len(temp2)):
        temp1.append(temp2[k])
    temp1.sort()
    cnt = 0
    flag = 1
    for k in range(1, len(temp1)):
        if temp1[k][0] == flag:
            cnt += 1
        else:
            flag = temp1[k][0]

    print(cnt)





