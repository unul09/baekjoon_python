# 2447 (나중에 다시)
# 출처 https://cotak.tistory.com/38

def paint_star(LEN):
    DIV3 = LEN//3

    if LEN == 3:    # LEN이 3까지 쪼개졌을 때 아래 값 넣는다
        g[1] = ['*', ' ', '*']
        g[0][:3] = g[2][:3] = ['*']*3
        return  # 전의 재귀함수으로 탈출

    paint_star(DIV3)    # 재귀

    for i in range(0, LEN, DIV3):   # 3개 영역
        for j in range(0, LEN, DIV3):   # 3개 영역
            if i == DIV3 and j == DIV3:    # 가운데 영역이면 패스
                continue
            for k in range(DIV3):   # 가운데 영역 아니라면
                g[i+k][j:j+DIV3] = g[k][:DIV3]  # 그 영역을 0,0 영역과 복사해서 채우기


n = int(input())

# 공백으로 채워진 n*n 크기 배열 생성
g = [[' ' for _ in range(n)] for _ in range(n)]

paint_star(n)

# 출력
for i in range(n):
    for j in range(n):
        print(g[i][j], end='')
    print()