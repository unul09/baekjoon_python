# 2437
# n-1번까지의 합 < n번째수 일때, 측정할수 없는 최소값은 (n-1번까지의 합 + 1)
import sys
N = int(sys.stdin.readline())
scales = list(map(int, sys.stdin.readline().split()))

scales.sort()

# 첫번째 값이 1이 아닐경우 바로 나가리
if scales[0] != 1:
    print(1)
    exit()

sum_scales = 0
for i in range(N-1):
    sum_scales += scales[i] # 합계 구하기
    if sum_scales + 1 < scales[i+1]: # 합계+1 보다 다음수가 더 크다면, 그 사이 갭이 있다는 말
        print(sum_scales + 1)
        exit()

sum_scales += scales[N-1] + 1 # 중간 갭 없이 연속적으로 모든 수가 나타날 경우, 수열 총합 +1 리턴
print(sum_scales)