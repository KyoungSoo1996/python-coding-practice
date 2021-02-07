# 이진 탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있다.
# 이진 탐색은 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있다.
# 이진 탐색은 위치를 나타내는 변수 3개를 사용하는데 탐색하고자 하는 범위의 시작점, 끝점, 중간점이다.
# 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 게 이진 탐색 과정이다.
numbers = [0,18,2,16,4,14,6,12,8,10]

#SelectSort

def SelectSort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i,len(numbers)):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

def InsertSort(numbers):
    for i in range(len(numbers)):
        for j in range(i, 1, -1):
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            else:
                break
    return numbers

def quickSort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    tail = numbers[1:]
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    return quickSort(left) + [pivot] + quickSort(right)


    
def binarySearch(numbers, findNum):
    numbers = quickSort(numbers)
    return binary_Search(numbers, findNum, numbers[0], numbers[-1])

def binary_Search(numbers, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if numbers[mid] == target:
        return mid
    elif numbers[mid] > target:
        return binary_Search(numbers, target, start, mid-1)
    else:
        return binary_Search(numbers, target, mid+1, end)


print(binarySearch(numbers,6))
