def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr2)):
                temp += arr1[i][k] * arr2[k][j]
            answer[i][j] = temp
    return answer


testArr1 = [[1, 4], [3, 2], [4, 1]]
testArr2 = [[3, 3], [3, 3]]
testArr3 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
testArr4 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
arr1 = [[1, 2, 3], [4, 5, 6]]
arr2 = [[1, 4], [2, 5], [3, 6]]


print(solution(testArr1, testArr2))
