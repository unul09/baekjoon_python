# 7568

N = int(input())
rank = []
for _ in range(N):
    rank.append(list(map(int, input().split())))

result = []

for current in rank:
    personal_rank = 1
    for compare in rank:
        if current[0]<compare[0] and current[1]<compare[1]:
            personal_rank += 1
    result.append(personal_rank)


print(' '.join(map(str, result)))
