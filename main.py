# 1541 개선ver
"""
식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있음

마이너스 기호 만나기 전, 후로 나누어
전의 수는 더하기로 처리
후의 수는 빼기로 처리
"""
arr = input().split('-')
s = 0
for i in arr[0].split('+'):
    s += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)



