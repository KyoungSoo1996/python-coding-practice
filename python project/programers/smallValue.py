def solution(A,B):
    answer = 0
    A = sorted(A, reverse= True)
    B = sorted(B)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer

testA = [1,4,2]
testB = [5,4,4]
print(solution(testA,testB))