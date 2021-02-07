# 회전판에 먹어야 할 N개의 음식이 있다.
# 각 음식에는 1부터 N까지 번호가 붙어있다.
# 음식을 섭취하는데 일정 시간이 소요된다.

# 무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓습니다.
# 마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 옵니다.
# 무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취합니다.
# 다음 음식 : 섭취해야 할 가장 가까운 번호의 음식
# 회전판이 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없다.

# 무지가 먹방을 시작한 지 K초 후에 네트워크 장애로 방송이 중단되었다.
# 방송이 정상화 후 다시 방송을 이어갈 때 며ㅕㅊ 번 음식부터 섭취해야 하는가?

food_times = [2,1,2]
k = 5

# # 시간 초과
# def solution(food_times, k):
#     answer = 0
#     sw = [1,-1]
#     select = False
#     count = 0
#     while sum(food_times) != 0:
#         if food_times[answer] > 0:
#             food_times[answer] -= 1
#             answer = answer + sw[select]
#             count += 1
#             if count == k + 1:
#                 return answer
#             if answer == len(food_times) -1:
#                 select = True
#             elif answer == 0:
#                 select = False           
#         else:
#             answer = answer + sw[select]
#             if answer == len(food_times) -1:
#                 select = True
#             elif answer == 0:
#                 select = False
#     answer = -1
#     return answer

    
# print(solution(food_times, k))

def solution(food_times, k):
    answer = 0
    
    return answer


print(solution(food_times, k))