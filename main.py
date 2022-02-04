# 11047
'''
N: 동전의 종류
K원을 만드는데 필요한 동전 개수의 최솟값을 출력
'''

N, K = map(int, input().split())

coins = []
for i in range(N):
    coins.append(int(input()))

coins.reverse()
currentCoin = 0
total = 0
while K != 0:
    if K < coins[currentCoin]:
        currentCoin += 1
    else:
        # 한번에 하나씩 빼주는건 시간 오래걸려서 시간초과 난다
        # 나머지, 나누기 활용하여 한번에 뺄 수량 다 빼주기
        total += int(K / coins[currentCoin])
        K = K % coins[currentCoin]

print(total)



