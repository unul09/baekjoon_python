# 1074
N, r, c = map(int, input().split())

start = 0
end = 4**N


while N > 0:
    boundery_size = (end-start)//4 # 4분할 크기
    # 범위 4개중 하나로 좁히는 과정의 반복
    if r < 2 ** (N - 1):
        if c < 2 ** (N - 1):
            end = start + boundery_size
        else:
            end = start + boundery_size * 2
            start = start + boundery_size

            c -= 2**(N-1) # 인덱스 스타팅포인트 범위 맞추어 수정
    else:
        r -= 2 ** (N - 1)
        if c < 2 ** (N - 1):
            end = start + boundery_size * 3
            start = start + boundery_size * 2

        else:
            start = start + boundery_size * 3
            c -= 2 ** (N - 1)

    N -= 1


print(start)

