def solution(dartResult):
    calc = ''
    for i in dartResult:
        if i == 'S':
            calc += '^1'
        elif i == 'D':
            calc += '^2'
        elif i == 'T':
            calc += '^3'
        elif i == '#':
            calc += '*(-1)'
            calc = calc.replace('+*','*')
        elif i == '*':
            temp = []
            for i in range(len(calc)):
                if calc[i] == '+':
                    temp.append(i)
            if(temp == []):
                calc += '*2+'
            elif(len(temp) == 1):
                calc += '*2+'
            temp = sorted(temp, reverse=True)[0:2]
            for i in temp:
                print(temp)
                restText = calc[i:]
                calc = calc[0:i] + '*2' + restText
        else :
            calc += i
        if i is not dartResult[-1] and (i =='S' or i == 'D' or i =='T' or i == '#'):
                calc += '+'
    calc = calc.rstrip('+').replace('^','**')
    return eval(calc)

def best_solution(dartResult):
    score = []
    n = ''
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            score.append(int(n) ** 1)
            n = ''
        elif i == 'D':
            score.append(int(n) ** 2)
            n = ''
        elif i == 'T':
            score.append(int(n) ** 3)
            n = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] *= 2
            score[-1] *= 2
        elif i == '#':
            score[-1] *= -1
    return sum(score)
    
testDart = '1S2D*3T'
testDart2 = '1D2S#10S'
testDart3 = '1D2S0T'
testDart4 = '1S*2T*3S'
testDart5 = '1D#2S*3S'
testDart6 = '1T2D3D#'
testDart7 = '1D2S3T*'
print(solution(testDart7))
print(best_solution(testDart7))
