def PlusOne(nums):
    return list(map(int, str(int(''.join(list(map(str, nums)))) + 1)))


def _PlusOne(nums):
    value = int(''.join(list(map(str, nums))))
    value += 1
    nums = list(map(int, str(value)))
    return nums


print(_PlusOne([1, 9, 9]))
# print(PlueOne([1, 9, 9]))

# * 가독성이 떨어지지만, 파이썬의 장점을 이용하기 위해 한줄로 다시 요약했습니다.
#   가독성이 좋게 쪼개놓은 코드도 첨부하겠습니다.
# 목표 : list를 하나의 숫자로 만들어 1을 더한 후, 다시 list로 변환한다.

# 1. nums를 str로 변환한 후, join하여 하나의 문자열로 만든다.
# 2. 하나의 문자열을 정수로 변환 후 1을 더해준다.
# 3. 1을 더해준 숫자를 문자열로 변환한다.
# 4. list로 변환하면서 map을 사용하여 각각 요소를 int형으로 변환해준다.
