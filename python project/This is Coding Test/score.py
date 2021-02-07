# 국어 점수가 감소하는 순서로
# 영어 점수가 증가하는 순서로
# 수학 점수가 감소하는 순서로
# 사전 순으로 증가하는 순서로

student = [
    ['Junkyu',50,60,100],
    ['Sangkeun',80,60,50],
    ['Sunyoung',80,70,100],
    ['Soong',50,60,90],
    ['Haebin',50,60,100],
    ['Kangsoo',60,80,100],
    ['Donghyuk',80,60,100],
    ['Sei',70,70,70],
    ['Wonseob',70,70,90],
    ['Sanghyun',70,70,80],
    ['nsj',80,80,80],
    ['Taewhan',50,60,90]
]

def SortStudent(student):
    answer = []
    for data in sorted(student, key= lambda x: (-x[1], x[2], -x[3], x[0])):
        answer.append(data[0])

    return answer



print(SortStudent(student))