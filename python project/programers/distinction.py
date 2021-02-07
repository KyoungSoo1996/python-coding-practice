def solution(s: str) -> bool:
    if s.isdigit() and (len(s) == 4 or len(s) == 6):
        answer = True
    else:
        answer = False
    return answer


def bestSolution(s: str) -> bool:
    return s.isdigit() and len(s) in(4, 6)


print(solution('a122'))
print(bestSolution('a122'))
