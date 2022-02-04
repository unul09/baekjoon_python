# 13305
# 이번 도착지에서의 기름이 더 싸면 그걸로 교체, 아닐시 유지
# 기름을 일정량 사서 소진하는 식으로 사고하면 안됨. 더 적은 기름값을 선택해서 운용한다고 사고하기

N = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))

nowPrice = price[0]
total = 0

for i in range(N-1):
    total += nowPrice * dis[i]
    if nowPrice > price[i+1]:
        nowPrice = price[i+1]

print(total)





