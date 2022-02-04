# 1339
'''
유의사항 + 해결방안
ABC + BCD
100A + 110B + 10C + D

처음에는 숫자.문자 매핑해서 하나하나 할당해주려 했는데
그럴 시에 위에 경우에 잘못된 값을 답으로 내놓게 됨
그러므로 그냥 수학적으로.!!! 접근하면.. 되는 것
'''
import math
import operator

N = int(input())

coef = {}
for _ in range(N):
    word = input()
    for i in range(len(word)):
        if not (word[i] in coef):
            coef[word[i]] = 0
        coef[word[i]] += int(math.pow(10, len(word)-1 - i))

coef_new = sorted(coef.items(), key=operator.itemgetter(1), reverse=True)

sum = 0
val = 9
for i in coef_new:
    sum += i[1] * val
    val -= 1

print(sum)

