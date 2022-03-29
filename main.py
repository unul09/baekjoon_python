# 2750

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()
nums_result = '\n'.join(map(str, nums))

print(nums_result)