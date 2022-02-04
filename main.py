# 11399

N = int(input())

bag = 0

while N%5 != 0:
    N -= 3
    bag += 1
    if N < 0:
        print(-1)
        exit()

bag += int(N/5)

print(bag)