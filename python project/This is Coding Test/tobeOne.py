d = [0] * 300001

def tobeOne(x):
    d = [0] * 300001
    for i in range(2, x+1):
        d[i] = d[i-1] + 1
        if i%2 == 0:
            d[i] = min(d[i], d[i//2] + 1)
        elif i%3 == 0:
            d[i] = min(d[i], d[i//3] + 1)
        elif i%5 == 0:
            d[i] = min(d[i], d[i//5] + 1)
    return(d[x])

print(tobeOne(26))
