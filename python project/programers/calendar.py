def solution(a, b):
    answer = ''
    days = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    answer = week[(4+ days[a - 1] + b) % 7]
    return answer

print(solution(5,24))
