# 다솜이는 이 문자열 s에 있는 모든 숫자를 전부 같게 만드려고 한다.
# S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는다.

# ex) S = 0001100일 경우, 전체를 뒤집으면 1110011이 된다.
#     4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 두 번 만에 모두 같은 숫자로 만들 수 있다.
#     그러나 4번째 문자에서 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.

# exText = '000000'

# def ReverseSTR(text):
#     ok = exText[0]
#     for i in text:
#         if ok != i:
#             return 1
#     return 0 

# print(ReverseSTR(exText))

# 연속된 숫자만 뒤집을 수 있다.

exText = '0001100'

# def ReverseSTR(text):
#     count0 = 0
#     count1 = 0
#     if text[0] == '1':
#         count0 +=1
#     else:
#         count1 +=1

#     for i in range(len(text) - 1):
#         if text[i] != text[i+1]:
#             if text[i+1] == '1':
#                 count0 +=1
#             else:
#                 count1 +=1
#     return min(count0, count1)
# print(ReverseSTR(exText))

def Reverse(text):
    count0 = 0
    count1 = 0
    if int(text[0]) == 1:
        count0 +=1
    else:
        count1 +=1
        
    for i in range(len(text) -1):
        if text[i] != text[i+1]:
            if int(text[i+1]) == 1:
                count0 +=1
            else:
                count1 +=1
    return min(count0, count1)

print(Reverse(exText))