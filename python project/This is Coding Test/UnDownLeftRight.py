# 여행가 A는 N X N 크기의 정사각형 공간 위에 서 있다.
# 이 공간은 1 X 1 크기의 정사각형으로 나누어져 있다.
# 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다.
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1) 이다.
# 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있다.
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀 있다.
# 각 문자의 의미는 다음과 같다. (해당 방향에 한 칸 씩 이동)
# 이때 여행가 A가 N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
# 예를 들어 (1, 1)의 위치에서 L 혹은 U를 만나면 무시된다.
# 다음은 N = 5인 지도와 계획서이다.
# 첫째 줄에 공간의 크기를 나타내는 N이 주어진다.(1 <= N <= 100)
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1 <= 이동 횟수 <= 100)

#start time : 3: 49

num = int(input())
mapping = list(map(str, input().split()))


up = 1
left = 1
for arrow in mapping:
    if arrow == 'U' and up > 1:
        up -= 1
    elif arrow == 'D' and up < int(num):
        up += 1
    elif arrow == 'L' and left > 1:
        left -= 1
    elif arrow == 'R' and left < int(num):
        left += 1
print(str(up) + ' ' + str(left))

#end time : 4:02