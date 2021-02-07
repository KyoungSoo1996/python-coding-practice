def solution(s):
    answer = ''
    temp = s.split(' ')
    for n in range(len(temp)):
        if n != 0:answer += ' '
        for num in range(temp[n].count('') - 1):
            if(num % 2 == 0):
                answer += temp[n][num].upper()
            else:
                answer += temp[n][num].lower()
        
    return answer

def best_solution(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])

print(solution('sf sdf'))
print(best_solution('sf sdf'))