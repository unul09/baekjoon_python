# 4796

caseCnt = 0
while True:
    caseCnt += 1
    L, P, V = map(int, input().split())
    if L == 0:
        break

    total = 0
    total += L * (V//P)
    V -= P * (V//P)
    if V < L:
        total += V
    else:
        total += L

    print("Case %d: %d" %(caseCnt, total))



