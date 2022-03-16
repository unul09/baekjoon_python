# 11729

def hanoi_number_of_moves(n):
    if n == 1: return 1
    return hanoi_number_of_moves(n-1)*2 + 1


def hanoi_seq_print(n, start, temp, end):
    if n == 0:
        exit()
    # n이 1이라면 시작점, 끝나는점 프린트
    elif n == 1:
        print(start, end)

    else:
        # n 짝수라면 n-1함수(end는 temp), 옮기기, n-1함수
        # n 홀수라면 n-1함수(end는 end), 옮기기, n-1함수
        hanoi_seq_print(n - 1, start, end, temp)
        print(start, end)
        temp, start = start, temp
        hanoi_seq_print(n - 1, start, temp, end)
        end, start = start, end


n = int(input())
print(hanoi_number_of_moves(n))
hanoi_seq_print(n, 1, 2, 3)