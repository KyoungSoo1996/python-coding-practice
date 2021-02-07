def TwoSum(nums, target):
    for index, num in enumerate(nums):
        if target - num in nums:
            return sorted([nums.index(target - num), index])


# 1. nums를 enumerate로 돌려, index와 num을 순차적으로 돌린다.
# 2. 목표 숫자와 num을 빼면서, 그 값이 nums에 포함되어 있는지 확인한다.
#     - nums안에 있는 숫자를 target과 빼서 nums 안에 있는 숫자가 나온다면,
#       결과적으로 두 수를 더한 값이 target인 셈이다.
#       [a + b = target] == [b = target - a]
# 3. 출력 값을 정렬하여 출력한다.

print(TwoSum([2, 7, 11, 15], 9))
