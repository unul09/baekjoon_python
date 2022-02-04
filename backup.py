words = []
words_int = []
N = int(input())
for _ in range(N):
    words.append(input())
    words_int.append("")

words.sort(key=lambda x: len(x), reverse=True)

for i in range(1, N):
    for j in range (len(words[0]) - len(words[i])):
        words[i] = ' ' + words[i]

alphaMap = {}
val = 9

for i in range(len(words[0])):
    for j in range(N):
        if words[j][i] == ' ':
            continue
        if not (words[j][i] in alphaMap):
            alphaMap[words[j][i]] = val;
            val -= 1
        words_int[j] += str(alphaMap[words[j][i]])


sum = 0
for i in words_int:
    sum += int(i)

print(sum)