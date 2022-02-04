# 1931
'''
N개의 회의
각 회의 I에 대해 시작시간과 끝나는 시간이 주어진다
'''

N = int(input())

meeting = []
for i in range(N):
    startTime, endTime = map(int, input().split())
    meeting.append([startTime, endTime])


'''
간과했던 점!!! 구글 검색으로 알아냄

시작과 끝이 같을 수 있기 때문에 
3 3 회의를 먼저 한다면 1 3 회의를 진행할 수 없지만 
1 3 회의를 먼저 한다면 3 3 회의를 진행할 수 있겠죠?

때문에 저희는 회의가 끝나는 시간을 우선순위로 먼저 정렬해준 뒤에 
그 순서 내에서 시작시간을 정렬해주어야 한답니다.
meeting.sort(key=lambda x: (x[1], x[0]))
'''
# 끝나는 시간 기준 오름차순 정렬
meeting.sort(key=lambda x: (x[1], x[0]))


clock = meeting[0][1]
index = 1
while True:

    if index == len(meeting):
        break
    if meeting[index][0] < clock:
        meeting.remove(meeting[index])
    else:
        clock = meeting[index][1]
        index += 1



print(len(meeting))




