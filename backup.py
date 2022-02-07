

N = int(input())
nums = [int(input()) for _ in range(N)]

total = 0

nums.sort()

if N % 2 == 1 and (nums[0] > 1 or nums[N-1] < 0):
    if nums[0] > 1:
        total += nums[0]
        nums.remove(nums[0])
    else:
        total += nums[N-1]
        nums.remove(nums[N-1])

for i in range(int(N / 2)):
    n1 = 2*i
    n2 = 2*i+1
    if (nums[n1] < 0 and nums[n2] <= 0) or (nums[n1] > 1 and nums[n2] > 1):
        total += nums[n1] * nums[n2]
    else:
        if N % 2 == 1:
            total += nums[n1]
            nums.remove(nums[n1])
        else:
            total += nums[n1] + nums[n2]

if N % 2 == 1:
    total += nums[len(nums)-1]


print(total)
