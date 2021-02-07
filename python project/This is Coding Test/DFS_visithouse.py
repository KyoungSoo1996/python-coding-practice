map = [
    [0,1,1,0,1,0,0],
    [0,1,1,0,1,0,1],
    [1,1,1,0,1,0,1],
    [0,0,0,0,1,1,1],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,1,0,0,0],
]

def DFS(x, y, num):
    if x < 0 or x >= len(map[0]) or y < 0 or y>= len(map):
        return False
    if map[x][y] == 1:
        map[x][y] = num
        DFS(x, y+1,num)
        DFS(x, y-1,num)
        DFS(x-1, y,num)
        DFS(x+1, y,num)
        return True
    return False

def DFS_visithouse(map):
    num = 2
    for i in range(0, len(map[0])):
        for j in range(0, len(map)):
            if DFS(i,j, num) == True:
                num += 1
    for i in range(0, len(map[0])):
        for j in range(0, len(map)):
            if map[i][j] != 0:
                map[i][j] -=1
    return map

print(DFS_visithouse(map))
