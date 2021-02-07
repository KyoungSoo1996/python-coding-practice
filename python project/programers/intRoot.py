def solution(n):
    sw = (n**0.5).is_integer()
    if sw:
        return (n**0.5 +sw * 1)**2
    else:
        return -1


print(solution(120))
