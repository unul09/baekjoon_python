# 10610
# 30의 배수 = 3의배수이면서 10의배수 = (각자릿수총합%3 ==0) and (일의자리수 0)

N = input()
nums = []
for i in range(len(N)):
    nums.append(int(N[i]))

nums.sort(reverse=True)

if (sum(nums) % 3 != 0) or (nums[len(nums) - 1] != 0):
    print(-1)
    exit()

for num in nums:
    print(num, end='')