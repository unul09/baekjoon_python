# 9020
import math


def isPrime(n):
    if n <= 3: return True
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True


T = int(input())
for _ in range(0, T):
    n = int(input())
    p1 = int(n / 2)
    p2 = n - p1

    while (not isPrime(p1)) or (not isPrime(p2)):
        p1 -= 1
        p2 += 1

    print(p1, p2)



