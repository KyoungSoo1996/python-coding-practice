# 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고,
#  그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복하면 어떨까?

a = [7,5,9,0,3,1,6,2,4,8]

def SelectSort(group):
    for num in range(len(group)):
        min_index = num
        for i in range(min_index+1, len(group)):
            if group[min_index] > group[i]:
                min_index = i
        group[min_index], group[num] = group[num], group[min_index]
    print(group)


print(SelectSort(a))