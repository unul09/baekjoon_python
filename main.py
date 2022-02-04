# 10162

T = int(input())

if T % 10 != 0:
    print(-1)
    exit()

print(int(T / 300), end=' ')
T = T % 300
print(int(T / 60), end=' ')
T = T % 60
print(int(T / 10))


