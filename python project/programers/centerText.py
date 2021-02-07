def solution(s):
    text =''
    if len(s) % 2 == 0:
        text = str(s)[(int)(len(s)/2) - 1] + str(s)[(int)(len(s)/2)]
    else:
        text = str(s)[(int)(len(s)/2)]
    answer = text
    return answer

print(solution('hello'))
