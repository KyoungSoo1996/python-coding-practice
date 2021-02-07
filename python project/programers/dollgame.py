def solution(board, moves):
    box = []
    answer = 0
    for num in moves:
        for i in range(0, len(board)):
            if board[i][num - 1] != 0:
                if len(box) == 0:
                    box.append(board[i][num - 1])
                    board[i][num - 1] = 0
                    break
                if box[-1] == board[i][num - 1]:
                    answer += 1
                    box.pop(-1)
                else:
                    box.append(board[i][num - 1])

                board[i][num - 1] = 0
                break
    return answer * 2


testBoard = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1],
             [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
testMoves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(testBoard, testMoves))
