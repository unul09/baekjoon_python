# 2480

dice = list(map(int, input().split()))
dice.sort()

if dice[0] == dice[1] and dice[1] == dice[2]:
    total = 10000 + dice[0]*1000
elif dice[0] == dice[1] or dice[1] == dice[2]:
    total = 1000 + dice[1]*100
else:
    total = dice[2]*100

print(total)