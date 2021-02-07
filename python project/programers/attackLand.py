land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1], [100, 0, 9, 8]]

# def solution(land):
#     answer = []
#     sumLand = 0
#     for i in land[0]:
#         no = land[0].index(i)
#         sumLand += i
#         for j in range(1, len(land)):
#             land[j][:no] + land[j][no + 1:]
#             sumLand += max(land[j][:no] + land[j][no + 1:])
#             no = land[j].index(max(land[j][:no] + land[j][no + 1:]))
#         answer.append(sumLand)
#         sumLand = 0
#     return max(answer)


def solution(land):
    for i in range(1, len(land)):
        land[i][0] = max(land[i][0] + land[i - 1][1],
                         land[i][0] + land[i - 1][2],
                         land[i][0] + land[i - 1][3])
        land[i][1] = max(land[i][1] + land[i - 1][0],
                         land[i][1] + land[i - 1][2],
                         land[i][1] + land[i - 1][3])
        land[i][2] = max(land[i][2] + land[i - 1][0],
                         land[i][2] + land[i - 1][1],
                         land[i][2] + land[i - 1][3])
        land[i][3] = max(land[i][3] + land[i - 1][0],
                         land[i][3] + land[i - 1][1],
                         land[i][3] + land[i - 1][2])
        print(land)
    return max(land[i])


print(solution(land))