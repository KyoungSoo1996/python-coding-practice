def solution(seoul):
    return "김서방은 "  + str(seoul.index('Kim')) +"에 있다"

def best_solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

testSeoul = ['Jane', 'Kim']

print(solution(testSeoul))
print(best_solution(testSeoul))