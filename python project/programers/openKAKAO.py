def solution(record):
    answer = []
    user = {}
    for i in record:
        tempLogic = i.split(' ')
        if tempLogic[0] == 'Enter':
            user[tempLogic[1]] = tempLogic[2]
        elif tempLogic[0] == 'Change':
            user[tempLogic[1]] = tempLogic[2]
    for i in record:
        tempLogic = i.split(' ')
        if tempLogic[0] == 'Enter':
            answer.append(user[tempLogic[1]] + "님이 들어왔습니다.")
        elif tempLogic[0] == 'Leave':
            answer.append(user[tempLogic[1]] + "님이 나갔습니다.")
    return answer


testRecord = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
              "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]

print(solution(testRecord))
