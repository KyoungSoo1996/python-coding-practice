def solution(nums):
    selectMax = len(nums)//2
    if selectMax <= len(set(nums)):
        return selectMax
    else :
        return len(set(nums))

def best_solution(nums):
    return min(len(nums)/2, len(set(nums)))

testNums = [3,1,2,3]
print(solution(testNums))
print(best_solution(testNums))