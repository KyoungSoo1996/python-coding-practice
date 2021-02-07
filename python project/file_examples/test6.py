def solution(phone_number):
    data = []
    count = 0
    for num in str(phone_number):
        if(count < len(str(phone_number)) - 4):
            data.insert(len(str(phone_number)), '*')
        else:
            data.insert(len(str(phone_number)), num)
        count += 1
    answer = data
    return answer


print(solution('01335352454325'))
