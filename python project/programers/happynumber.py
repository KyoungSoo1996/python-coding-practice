def HappyNumber(num):
    cycle = [sum(list(map(int, str(num))))]
    temp = num
    while cycle[-1] != 1:
        temp = sum([pow(i, 2) for i in list(map(int, str(temp)))])
        if temp in cycle:
            return False
        cycle.append(temp)
    return True


print(HappyNumber(1))

# 목표 : 숫자를 분해해서 제곱하여 더한다. 이를 반복하여 1이 나오면 True 아니면 False이다.
# 규칙 : 직접 계산해본 결과 HappyNumber가 되지 못하면, 연산 과정이 규칙적인 사실을 발견했다.
#        이를 사용하여 cycle이 나온다면 False를 출력하기로 했다.

# * 각 자리수를 제곱하여 더하는 행위를 PowSum이라 정의한다.
# 1. cycle에 인자값을 powsum하여 나온 결과를 넣고, temp에 인자값을 넣는다.
#     반복 (cycle의 마지막이 1이 아니면)
#         2. temp에 temp와 powsum 결과를 넣는다.
#             3. 만일 temp 값이 이미 cycle에 존재하면 Flase를 출력한다.
#         4. cycle에 temp를 추가한다.
# 5. cycle에 1이 발견될 경우 True를 출력한다.
