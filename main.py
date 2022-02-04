# 1931 개선ver

'''
문제해결 설명
데이터를 끝나는 시간 기준 내림차순, 끝나는 시간 같을경우에는 그 안에서 시작시간 내림차순 정렬
첫번째 데이터의 끝나는 시간 둔상태에서 리스트 한번 쫙~ 훝으며
적합한 회의라면(시작시간이 end time보다 크거나같다면) 회의수 카운트증가 + end time 갱신
'''

'''
반복문으로 여러줄 입력받는 상황에서는 
반드시 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않습니다.
'''
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n): # i 할당없이 단순 n번반복!
    data.append(list(map(int,input().split()))) #list로 만들어서 넣어주기!

data.sort(key=lambda x: (x[1], x[0]))

end_t = data[0][1]
cnt = 1


#리스트 변형 없이 그저 한번 훝어보기!!!
for i in range(1, n):  #두번째놈부터 볼거임
    if data[i][0] >= end_t:
        cnt += 1
        end_t = data[i][1]

print(cnt)