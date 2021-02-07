def solution(s):
    if len(s.split('p')) + len(s.split('P')) == len(s.split('y')) + len(s.split('Y')):
        return True
    else:
        return False


def bestSolution(s):
    return s.lower().count('p') == s.lower().count('y')


print(solution('happy'))
print(bestSolution('happy'))