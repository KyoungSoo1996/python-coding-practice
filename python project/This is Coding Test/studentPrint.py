# N 명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하시오.

# 첫 번째 줄에 학생의 수 N이 입력된다.
# 두 번째 줄부터 N + 1 번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
# 문자열 A의 길이와 학생의 성적은 100이하의 자연수이다.

# 2
# 홍길동 95
# 이순신 77



n = int(input())
student = []
for i in range(n):
    inputData = input().split()
    student.append((inputData[0], int(inputData[1])))

student = sorted(student, key = lambda x: x[1], reverse= True)

print(student)