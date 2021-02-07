# 각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어질 때, 숫자 사이에 X 혹은 + 연산자를 넣어
# 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

# 단, +보다 X를 먼저 계산하는 일반적인 방식이 아닌, 모든 연산은 왼쪽에서 이뤄진다.

str1 = '02984'
str2 = '567'


def PnP(str):
    result = 1
    for i in str:
        if int(i) <= 1:
            continue
        else:
            result *= int(i)
    return result

print(PnP(str2))