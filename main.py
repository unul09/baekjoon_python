# 2798

import itertools

N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards_3 = list(itertools.combinations(cards, 3))
card_sums = list(sum(card_sum) for card_sum in cards_3)

card_sums.sort()
for i in range(len(card_sums)):
    if card_sums[i] > M: # 초과하는 인덱스 바로 전의 값을 출력
        if i == 0: # 첫번째부터 초과할 경우, 첫번째가 출력되도록
            i += 1
        print(card_sums[i-1])
        exit()
    if i == len(card_sums)-1: # 마지막까지 M보다 작을 경우
        print(card_sums[i])
        exit()



