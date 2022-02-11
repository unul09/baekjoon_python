# 1080
# 60퍼센트까지 가다가 틀린다!!
# 문제 조건 제대로 해석할것. 3x3 미만크기 행렬에 대해 -1출력하라는 내용은 그 어디에도 없었음.

N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(N)]


cnt = 0

# 우측, 하단의 각 2줄은 딸려오는 놈들. 얘네 빼고 하나하나 비교해주며, 불일치할시 행렬뒤집기 실시
for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            cnt += 1
            for ii in range(3):
                for jj in range(3):
                    A[i + ii][j + jj] = '1' if A[i + ii][j + jj] == '0' else '0'


for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            print(-1)
            exit()

print(cnt)