# 1202
import heapq
import sys

N, K = map(int, sys.stdin.readline().split())

jewelryList = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bagList = [int(sys.stdin.readline()) for _ in range(K)]

# 보석, 가방 오름차순 정렬
jewelryList.sort()
bagList.sort()

# 우선순위힙 사용하여 result에 음수값으로 첨가해줄 것.
# 일시적 보석보관 장소 및 보석보관 확인용으로 temp리스트 쓸것.
result = 0
temp = []


for bagWeight in bagList:   # 가장 가벼운 가방부터, 보석보다 가방이 먼저 소진될경우 끝내기
    while jewelryList and bagWeight >= jewelryList[0][0]: # 가방한도 내에서 최대가치까지 돌릴거야
        # 가치를 음수로 만들어서 최대 음수(최대 가치)가 될때까지 넣.빼 할거
        heapq.heappush(temp, -jewelryList[0][1])  # Max heap
        heapq.heappop(jewelryList)

    if temp:
        # 가방에 보석이 담겼다면 그것은 최적의 보석. result에 넣기 / 없다면 충족보석 없으므로 패스
        result += heapq.heappop(temp)
    elif not jewelryList: #가방보다 보석이 먼저 소진될경우 끝내기
        break

print(-result)