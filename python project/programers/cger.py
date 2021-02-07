def solution(s, n):
    big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    answer = ''
    for i in range(len(s)):
        t = ord(s[i])
        if s[i] == ' ':
            answer += ' '
        if  t >= 65 and t <=91:
            answer += str(big[(big.index(s[i])+n)%26])
            #대문자
        elif t >=97 and t <=122:
            #소문자
            answer += str(small[(small.index(s[i])+n)%26])
    return answer


#한계 소문자 = 122, 대문자 = 91
#시작 소문자 = 97, 대문자 = 65
print(solution("z", 1))
