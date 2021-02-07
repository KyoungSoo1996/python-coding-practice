# 첫째 줄에 정수 N이 주어진다.
# 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다.
# 셋째 줄에는 정수 M이 주어진다.
# 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다.
# 상품이 있을 경우 yes를 없을 경우 no를 출력한다.

#start_time = 8:29
allComponent = [8, 3, 7, 9, 2]
wantCompoenent = [5, 7, 9]

def QuickSort(number):
    if len(number) <= 1:
        return number
    pivot = number[0]
    tail = number[1:]
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    return QuickSort(left) + [pivot] + QuickSort(right)

def Binary_search(number, target, start, end):
    if start > end:
        return 'no'
    mid = (start+end)//2
    if target == number[mid]:
        return 'yes'
    elif target < number[mid]:
        return Binary_search(number, target, start, mid-1)
    else:
        return Binary_search(number, target, mid+1, end)

def SearchingComponent(number, target):
    answer = []
    number = QuickSort(number)
    for i in target:
        answer.append(Binary_search(number, i, 0, len(number)))
    return answer

print(SearchingComponent(allComponent, wantCompoenent))

#end_time = 8:41