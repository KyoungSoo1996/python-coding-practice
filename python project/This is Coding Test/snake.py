# 게임은 N X N 정사각 보드 위에서 진행된다.
# 몇몇 칸에는 사과가 놓여져 있다.
# 상하좌우 끝에는 벽이 있다.
# 시작 할 때 위치는(0,0)이며, 뱀의 길이는 1이다.

# 뱀의 규칙
# - 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킨다.
# - 이동한 칸에 사과가 있다면, 그 칸의 사과는 없어지고 꼬리는 움직이지 않는다.
# - 이동한 칸에 사과가 없다면, 몸 길이를 줄여 꼬리가 위치한 칸을 비워준다.

# 입력 규칙
# 보드의 크기 N, 사과의 개수 K
# 사과의 위치 (행, 열) - K개
# 다음 줄에는 밤의 방향 변환 횟수 L이 주어진다.
# (시간, 방향) 방향 = L(왼쪽), D(오른쪽)

N = 10

K = 5
apples =[
    [1,5],
    [1,3],
    [1,2],
    [1,6],
    [1,7]
]

M = 4
snakeMoves = [
    [8,'D'],
    [10,'D'],
    [11,'D'],
    [13,'L']
]


def Snake(N, apples, snakeMoves):
    answer = 0
    # Map Maker
    gameMap = [[0] * N for i in range(N)]
    
    # Arrangment Apple
    for apple in apples:
        gameMap[apple[0]][apple[1]] = 1
    
    #make snake
    snake = [[0,0]]
    sw = False
    temp = [0,0]
    #snake arrow
    #right(0) -> down(1) -> left(2) -> up(3)
    arrow = 0
    moveX = [1,0,-1,0]
    moveY = [0,1,0,-1]
    #pred time
    pred = 0
    # game End
    for move in snakeMoves:
        # moving
        for time in range(pred, move[0]):            
            # snake Moving
            print(time)
            #eat apple
            # head condition
            if snake[0][0] + moveY[arrow] < 0 or snake[0][0] + moveY[arrow] >= N or snake[0][1] + moveX[arrow] < 0 or snake[0][1] + moveX[arrow]  >= N or gameMap[snake[0][0] + moveY[arrow]][snake[0][1] + moveX[arrow]] == 2:
                return time
                
            if gameMap[snake[0][0] + moveY[arrow]][snake[0][1] + moveX[arrow]] == 1 and sw == False:
                print('eat')
                gameMap[snake[0][0] + moveY[arrow]][snake[0][1] + moveX[arrow]] = 0
                temp = snake[0]
                sw = True

            for s in snake:
                gameMap[s[0]][s[1]] = 0
                s[1] = s[1] + moveX[arrow]
                s[0] = s[0] + moveY[arrow]
                gameMap[s[0]][s[1]] = 2

            if sw:
                snake.append(temp)
                sw = False 

            
            for i in gameMap:
                print(i)
            print('-------------------------')
            # snake arrowing
            if pred != move[0]:
                if pred != 0:
                    if move[1] == 'D':
                        arrow = abs(arrow+1)%5
                    else:
                        arrow = abs(arrow-1)%5
                pred = move[0]
            
    return time +1


print(Snake(N, apples, snakeMoves))
