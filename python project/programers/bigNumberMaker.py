#시간 초과로 실패
# def solution(number, k):
#     count = 0
#     while count < k:
#         temp = []
#         for i in range(len(number)):
#             tempText = ''
#             for j in range(len(number)):
#                 if i != j:
#                     tempText += number[j]
#             temp.append(tempText)
#         number = max_val(temp)
#         count += 1
#     return number

# def max_val(arr):
#     maxNum = arr[0]
#     for i in range(1,len(arr)):
#         if maxNum < arr[i]:
#             maxNum = arr[i]
#     return maxNum

def solution(number, k):
    temp = []
    for i, j in enumerate(number):
        while len(temp) > 0 and temp[-1] < j and k > 0:
            temp.pop()
            k -= 1
        if k <= 0:
            temp += list(number[i:])
            break
        temp.append(j)
    if k > 0 :
        temp = temp[:-k]
    else :
        temp
    return ''.join(temp)




testNumber = '0101010'
testK = 5

print(solution(testNumber, testK))
