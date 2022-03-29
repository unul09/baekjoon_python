# 1018

standard_chessboard = []
for i in range(8):
    if i % 2 == 0:
        standard_chessboard.append(list('WBWBWBWB'))
    else:
        standard_chessboard.append(list('BWBWBWBW'))

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))

color_min = 64
for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for a in range(8):
            for b in range(8):
                if board[i+a][j+b] != standard_chessboard[a][b]:
                    cnt += 1
        if cnt > 32: cnt = 64 - cnt
        if color_min > cnt: color_min = cnt

print(color_min)
