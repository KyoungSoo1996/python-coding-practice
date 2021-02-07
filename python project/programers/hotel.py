import sys
sys.setrecursionlimit(10**6)


def solution(k, room_number):
    answer = []
    dic = {}
    for num in room_number:
        answer.append(searchRoom(num, dic))
    return answer


def searchRoom(num, rooms):
    if num not in rooms:
        rooms[num] = num + 1
        return num
    empty = searchRoom(rooms[num], rooms)
    rooms[num] = empty + 1
    return empty


print(solution(10, [1, 3, 4, 1, 3, 1]))
