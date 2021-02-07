# 가로 길이가 N, 세로 길이가 2인 직사각형 형태의 얇은 바닥이 있다.
# 이 타일을 1X2, 2X1, 2X2로 채우고자한다.
# 이 바닥을 채우는 모든 경우의 수를 구하시오

def tileWork(lenght):
    d = [0] * 1001
    d[1] = 1
    d[2] = 3
    for i in range(3, lenght+1):
        d[i] = (d[i-1] + 2 * d[i-2]) % 796796
    return d[lenght]

print(tileWork(101))
