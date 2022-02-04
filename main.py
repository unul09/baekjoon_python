# 5585

M = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]
index = 0
total = 0
while M != 0:
    if M >= coin[index]:
        total += int(M / coin[index])
        M = M % coin[index]

    index += 1

print(total)
