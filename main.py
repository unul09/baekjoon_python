# 1715
'''
자료구조 종류, 각각 동작원리와 시간복잡도 공부할것
'''
import heapq # 우선순위 큐

N = int(input())

cardList = list(int(input()) for _ in range(N))
heapq.heapify(cardList)
result=0


while len(cardList) != 1:
    num1 = heapq.heappop(cardList)
    num2 = heapq.heappop(cardList)
    Sum = num1 + num2
    result += Sum
    heapq.heappush(cardList,Sum)

print(result)
