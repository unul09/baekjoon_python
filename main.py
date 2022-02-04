# 1541
"""
식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있음

"""
import re
exp = input()

numbers = re.findall(r'\d+', exp)
chars = re.sub(r'[0-9]+', '', exp)

ans = int(numbers[0])

if len(numbers) == 1:
    print(ans)
    exit()

# 마이너스가 하나라도 나오는 순간부터 그 위는 다 마이너스로 처리 가능
minus_Flag = False
for i in range(len(chars)):
    if chars[i] == '-':
        minus_Flag = True

    if minus_Flag:
        ans -= int(numbers[i+1])
    else:
        ans += int(numbers[i+1])


print(ans)




