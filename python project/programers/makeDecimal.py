import itertools


def decimalSearching(num):
    l = list(range(2, num + 1))
    k = int(num ** 0.5) + 1
    for i in range(2, k):
        t = 2
        pro = 0
        while pro < num:
            pro = t * i
            t += 1
            if pro in l:
                l.remove(pro)
    return l


def solution(nums):
    answer = 0
    maked_nums = []
    contain = list(itertools.combinations(nums, 3))
    for i in contain:
        maked_nums.append(sum(i))
    limit = decimalSearching(max(set(maked_nums)))
    for i in range(len(maked_nums)):
        if maked_nums[i] in limit:
            answer += 1
    return answer


testList = [1, 2, 3, 4]
print(solution(testList))
decimalSearching(10)
