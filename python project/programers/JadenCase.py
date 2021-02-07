def solution(s):
    answer = ''
    s = s.lower()
    temp = s.split(' ')
    for n in temp:
        if n == '':
            answer += ' '
        else:
            if n[0].isalpha():
                if n is not temp[0]:
                    answer += ' '
                n = n.capitalize()
                answer += n
            else :
                if n is not temp[0]:
                    answer += ' '
                answer += n

    return answer

def best_solution(s):
    return s.title()



testS = "for the  last week"
print(solution(testS))
print(best_solution(testS))