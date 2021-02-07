# 현재 캐릭터의 점수를 N이라고 할 때,
# 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합이
# 더한 값이 동일한 상황을 말한다.

# ex) 현재 점수가 123,402일 경우, 1+2+3 = 4+-+2 이므로 럭키 스트레이트를 사용할 수 있다.
#     현재 스코어가 입력되면, 사용할 수 있는 상태인지 알려주는 프로그램

def Lucky(score):
    data = list(map(int, list(str(score))))
    print(data)
    if sum(data[0:len(data)//2]) == sum(data[len(data)//2:]):
        return 'LUCKY'
    return 'READY'

print(Lucky(7755))

