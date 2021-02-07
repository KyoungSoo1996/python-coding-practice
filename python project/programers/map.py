def solution(n, arr1, arr2):
    answer = []
    oneArr = []
    twoArr = []
    #이진수로 변환
    for i in range(n):
        answer.append('')
        oneArr.append("{0:b}".format(arr1[i]).zfill(n))
        twoArr.append("{0:b}".format(arr2[i]).zfill(n))
    #리스트 융합 및 변경
    for i in range(n):
        for j in range(n):
            if (int(oneArr[i][j]) or int(twoArr[i][j])) == 1:
                answer[i] += '#'
            else:
                answer[i] += ' '
    return answer


def best_solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
            a12 = str(bin(i | j)[2:])
            a12 = a12.rjust(n, '0')
            a12 = a12.replace('1', '#')
            a12 = a12.replace('0', ' ')
            answer.append(a12)
    return answer


testn = 6
testArr1 = [46, 33, 33, 22, 31, 50]
testArr2 = [27, 56, 19, 14, 14, 10]

print(solution(testn, testArr1, testArr2))
print(best_solution(testn, testArr1, testArr2))
