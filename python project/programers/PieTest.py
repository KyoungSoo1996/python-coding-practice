#n명이 파이를 먹고 싶다고 가정했을 때
#각각이 먹게 될 파이의 비율을 반환하자

def pie_percent(n: int) -> int:
    return int(1/n * 100)

print(pie_percent(3))