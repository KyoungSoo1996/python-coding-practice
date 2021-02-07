def solution(arrangement):
    answer = 0
    stack = []
    for tag in range(len(arrangement)):
        if arrangement[tag] == "(":
            stack.append(arrangement[tag])

        else:
            stack.pop()

            if arrangement[tag - 1] == "(":
                answer += len(stack)
            else:
                answer += 1

    return answer


testArrangement = "()(((()())(())()))(())"
print(solution(testArrangement))
