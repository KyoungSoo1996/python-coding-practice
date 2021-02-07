
def solution(array: list, commands: list):
    answer = []
    temp = []
    for i in range(len(commands)):
        for j in range(commands[i][0], commands[i][1] + 1):
            temp.append(array[j-1])
        answer.append(sorted(temp)[commands[i][2]-1])
        temp.clear()
    return answer


def best_solution(array, commands):
                  return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


testarray = [1, 5, 2, 6, 3, 7, 4]
testcommands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(testarray, testcommands))
print(best_solution(testarray, testcommands))