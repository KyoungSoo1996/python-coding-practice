# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야한다.
# 첫째 줄에 모험가의 수 N이 주어진다. (1 <= N <= 100,000)
# 둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어진다.

l = [2, 3, 1, 2, 2, 4, 3, 2, 1, 4, 2, 3]


def guild(menber):
    d = sorted(menber)
    result = 0
    count = 0
    for i in d:
        count += 1
        if i <= count:
            result += 1
            count = 0
    return result


print(guild(l))
