# 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하여라.
# 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다.
# 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상이므로 손님은 필요한 양만큼 떡을 사갈 수 있다. 
# 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

# 적어도 M 만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

#start_time = 8:57
want_Lenght = 6
riceCake = [19, 15, 10, 17]

# def CutRiceCake(riceCake, want_Lenght):
#     riceCake = sorted(riceCake)
#     for i in range(riceCake[-1], 1, -1):
#         sumLenght = 0
#         for j in riceCake:
#             if j > i:
#                 sumLenght += (j - i)
#         if sumLenght >= want_Lenght:
#             return i


# print(CutRiceCake(riceCake,want_Lenght))
#end_time = 9:03

def CutRiceCake(riceCake, want_Lenght):
    riceCake = sorted(riceCake)
    start = riceCake[0]
    end = riceCake[-1]
    result = 0
    while(start <= end):
        total = 0
        mid = (start+end)//2
        for x in riceCake:
            if x > mid:
                total += x - mid
        if total < want_Lenght:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

print(CutRiceCake(riceCake,want_Lenght))


