# 1744

# 요소를 이득인거 순으로 다 제거해주며 리스트 비운다.

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

total = 0
index = 0
while len(nums) > 1:
    # 앞뒤로 살펴서 더 이득인쪽 먼저 해줄거임. 같을시엔 앞부터(왜냐? 그냥 이 식은 애초에 앞에서부터 하는걸 전제로 짰으니까 ...)
    n = len(nums)-2
    if nums[0] * nums[1] >= nums[n] * nums[n+1]:
        n = 0
    sum = nums[n] + nums[n+1]
    mul = nums[n] * nums[n+1]
    if mul >= sum: # 곱 더해주는게 더 이득
        total += mul
        nums.pop(n)
        nums.pop(n)
    else: # 합 더해주는게 더 이득
        if len(nums) % 2 == 1: # 홀수길이 놈이면 앞쪽 빼서 처리
            total += nums.pop(n)
        else:
            total += sum
            nums.pop(n)
            nums.pop(n)

# 마지막 한개 안빠져있는 경우 있기에 추가
if len(nums) == 1:
    total += nums.pop(0)


print(total)



