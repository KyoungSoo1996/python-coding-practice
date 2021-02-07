def divisor(num):
    temp = []
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            temp.append(i)
    return set(temp)


def solution(w, h):
    a = max([w, h])
    num = min([w, h])
    n = 9999999
    while True:
        n = a % num
        if n == 0:
            break
        else:
            a = num
            num = n
    return (w * h) - ((int(h / (h / num)) * (int(w / num + h / num) - 1)))


testW = 8
testH = 12
print(solution(testW, testH))
