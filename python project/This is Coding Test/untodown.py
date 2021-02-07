# 하나의 수열에는 다양한 수가 존재한다.
# 이러한 수는 크기에 상관없이 나열되어 있다.
# 이 수를 큰 수부터 작은 수의 순서대로 정렬해야 한다.
# 수열을 내림차순으로 정렬하는 프로그램을 만드시오.

numbers = [15, 27, 12]

# 선택 정렬
def SelectSort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i,len(numbers)):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[min_index], numbers[i] = numbers[i], numbers[min_index]
    return numbers[::-1]

# 삽입 정렬
def InsertSort(numbers):
    for i in range(len(numbers)):
        for j in range(i, 1, -1):
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            else:
                break
    return numbers[::-1]

# 퀵 정렬
def quickSort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    tail = numbers[1:]
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    return quickSort(left) + [pivot] + quickSort(right)

# 계수 정렬
def CountSort(numbers):
    result = []
    countList = [0] * (max(numbers) + 1)
    for i in numbers:
        countList[i] += 1

    for i in range(len(countList)):
        for j in range(0,countList[i]):
            result.append(i)
    return result[::-1]

print(SelectSort(numbers))
print(InsertSort(numbers))
print(quickSort(numbers)[::-1])
print(CountSort(numbers))