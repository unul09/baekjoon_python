while True:
    clock = meeting[0][1]
    total += 1
    if_flag = False
    for i in range(len(meeting)):
        if meeting[i][0] >= clock:
            meeting = meeting[i-1:]
            if_flag = True
            break

    if not if_flag:
        break


    '''
    # meeting배열에서 현재시각(clock)보다 이른 놈들 삭제
    temp = []
    for i in range(len(meeting)):
        if meeting[i][0] >= clock:
            temp.append(meeting[i])

    if len(temp) == 0:
        break
    meeting = temp
    '''

