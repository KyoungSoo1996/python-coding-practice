import heapq
#heapq모듈은 이진트리 기반의 최소 힙 자료구조를 제공한다


#heapq 안쓰면 시간초과 난단다
# def solution(scoville, K):
#     answer = 0
#     mixScoville = 0
#     scoville = sorted(scoville)
#     while scoville[0] < K:
#         if len(scoville) < 2:
#             return -1
#         mixScoville = scoville.pop(0) + scoville.pop(0) * 2
#         scoville.append(mixScoville)
#         scoville = sorted(scoville)
#         answer +=1
#     return answer

#using heapd
#heapify => 리스트를 힙으로 바꿔주는 친구(자동으로 정렬되나봄)
#heappop => 힙을 내보내주는 친구

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < k:
        if len(scoville) < 2:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer +=1
    return answer


testScoville = [1,2,3,9,10,12]
tsetK = 7

print(solution(testScoville, tsetK))