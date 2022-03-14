# 2525

A, B = map(int, input().split())
C = int(input())

H = A
M = B+C

while M >= 60:
    M -= 60
    H += 1

    if H >= 24:
        H -= 24

print(H, M)
