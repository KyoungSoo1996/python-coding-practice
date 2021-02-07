def solution(s):
    answer = False
    temp = ''
    while True:
        if s.count('(') != s.count(')'):
            answer = False
            break
        s = s.replace('()', '')
        if len(s) == 0:
            answer = True
            break
        if temp != s:
            temp = s
        else :
            answer = False
            break
    return answer

def best_solution(s):
    num = 0
    for item in s:
        if num < 0:
            return False
        if item == "(":
            num += 1
        else :
            num -= 1
    if not num:
        return True
    else:
        return False


testS = '(()))'
print(solution(testS))
