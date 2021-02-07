import time

# 지난 시간에 알아본 선택 정렬은 자신보다 작은 수를 찾아 위치를 서로 바꿔주는 형태였다.
# 즉 코딩을 해보자면 다음과 같다.
# 이 선택 정렬은 처음에 쓸만하지만, 점차 숫자가 늘어나면, 시간이 기하급수적으로 증가한다.
# 대충 10000개의 숫자를 정렬하는데 15초가 걸린다.
# 기본적으로 사용하는 sort 보다 효율이 떨어진다.

a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def SelectSort(group):
    start_time = time.time()
    for i in range(len(group)):
        min_index = i
        for j in range(min_index, len(group)):
            if group[min_index] > group[j]:
                min_index = j
        group[min_index], group[i] = group[i], group[min_index]
    end_time = time.time()
    return group, end_time - start_time

print(SelectSort(a))


# 이보다 조금 더 효율이 좋은 삽입 정렬은 다음과 같이 구현한다.
# 시작은 2번째부터 시작해서 끝부터 앞으로 가면서 자신보다 크면 넘어가고, 작으면 그 자리에 머문다.
# 그러면서 끝날 때 까지 반복하는 것이다.
# 자 그럼 삽입 정렬을 구현해보자.

def InsertSort(group):
    for i in range(1, len(group)):
        for j in range(i, 0, -1):
            if group[j] > group[j-1]:
                group[j], group[j-1] = group[j-1], group[j]
            else:
                break
    return group

print(InsertSort(a))
    
# 삽입 정렬과 선택 정렬의 복잡도는 N^2으로 똑같지만,
# 삽입 정렬은 이미 정렬된 데이터가 많을 경우 큰 효율을 낸다.
# 그러므로 이미 정렬되어있는 문제가 주어진다면, 삽입 정렬을 활용하는 것이 큰 효율을 낸다.