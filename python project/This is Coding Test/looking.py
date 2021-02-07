# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
# 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다.
# 00시 00분 03초
# 00시 13분 30초
# 반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안되는 시각이다.
# 00시 02분 55초
# 01시 27분 45초

# 첫째 줄에 정수 N이 입력된다.
# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.

#start time : 4:08
# 03, 13, 23, 33, 43, 53
# 59  59  59  59  59  59


# 59  59  59  59  59  59 
# 03, 13, 23, 33, 43, 53
# 3 time hour : 3540

N = int(input())
result = 0
for i in range(0, N-1):
    if i  in (3 ,13 , 23):
        result += 2025
    else:
        result += 3150
        
# for i in range(0, N + 1):
#     for j in range(0, 60):
#         for k in range(0, 60):
#             temp = list(str(i)+str(j)+str(k))
#             if '3' in temp:
#                 result += 1
print(result)

#end time : 4:25