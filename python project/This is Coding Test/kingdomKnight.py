# 행복 왕국의 왕실 정원은 체스판과 같은 8 X 8 좌표 평면이다. 왕실 정원의 특정한 한 칸에 나이트가 서 있다.
# 나이트는 매우 충성스러운 신하로서 매일 무술을 연마한다.
# 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
# 나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.

# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

# 이처럼 8 X 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
# 이때 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현한다.

#start time : 4:37

text = list(input())
xpos = ['a','b','c','d','e','f','g','h']
result = 0
pos = [int(xpos.index(text[0])), int(text[1]) -1]
moveBig = [2, -2]
moveSmail = [1, -1]

for moveX in moveBig:
    for moveY in moveSmail:
        if pos[0] + moveX >= 0 and pos[0] + moveX <= 8 and pos[1] + moveY >= 0 and pos[1] + moveY <= 8:
            result += 1
for moveY in moveBig:
    for moveX in moveSmail:
        print(str(pos[0] + moveX) + ' ' + str(pos[1] + moveY))
        if pos[1] + moveY >=0 and pos[1] + moveY <= 8 and pos[0] + moveX >=0 and pos[0] + moveX <= 8:
            result += 1
print(result)

#end time : 4:53
