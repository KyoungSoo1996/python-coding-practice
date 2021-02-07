#1. 함수 디자인 방법에 따라 매개변수가 숫자 하나이고 그 숫자의 3배를 반환하는 함수를 정의하시오
def three_pow(n : int)-> int:
    return n * 3

#2. 함수 디자인 방법에 따라 매개변수가 숫자 두 개이고, 두 숫자 간 차이의 절댓값을 반환하는 함수를 정의하시오.
def between_abs(a : int, b : int) -> int:
    return (abs(a - b))

#3. 함수 디자인 방법에 따라 매개변수가 킬로미터 단위의 거리 하나이고, 그 거리를 마일 단위로 바꿔 반환하는 함수를 정의하시오.
#1마일은 1.6킬로미터입니다.
def km_to_mile(km : float) ->float:
    return km * 1.6

#4. 함수 디자인 방법에 따라 매개변수가 세 개이고, 각각 0부터 100까지의 점수이며, 세 점수의 평균을 반환하는 함수를 정의하시오.
def three_average(a : float, b : float, c : float ) -> float:
    return (a + b + c) /3 

#5. 함수 디자인 방법에 따라 매개변수가 네 개이고, 각각 0부터 100까지의 점수이며 그중 상위 세점수의 평균을 반환하는 함수를 정의하시오.
#def best_three_average(a : float, b : float, c : float, d : float) -> float:

print(three_pow(3))
print(between_abs(10,-10))
print(km_to_mile(10.3))
print(three_average(2,90,50))

