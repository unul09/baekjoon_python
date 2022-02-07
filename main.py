# 1202
'''
<스스로 작성 개요>
sys.stdin.readline()
리스트 = [list() for _ in range()]
오름차순 정렬 후, 결과와 temp 리스트 생성
가장 가벼운 가방부터 돌 것.
가방한도 내에서 최대가치까지 돌릴거야. 가치를 음수로 만들어서 최대 음수(최대 가치)가 될때까지 넣.빼 할거
가방에 보석이 담겼다면 그것은 최적의 보석. result에 넣기 / 없다면 충족보석 없으므로 패스
가방보다 보석이 먼저 소진될경우 끝내기

<포인트>
무게에 대한 것은 오름차순, 가격에 대한 것은 내림차순으로 처리 -> 내림차순: 우선순위힙을 max값 받아오는 식으로 변경
낮은 무게에서 여러개가 필요하게 되는 조건 충족시키기 -> temp 활용하여 우선순위힙에 돌릴 값 넣어두기
'''

import heapq
import sys

N, K = map(int, sys.stdin.readline().split())

gems = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = [int(sys.stdin.readline()) for _ in range(K)]

gems.sort()
bags.sort()

result = 0
temp = []

for bag in bags:
    while gems and bag >= gems[0][0]:
        heapq.heappush(temp, -gems[0][1])
        heapq.heappop(gems)

    if temp:
        result += heapq.heappop(temp)

    elif not gems:
        break

print(-result)