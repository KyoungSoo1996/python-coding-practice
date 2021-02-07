user_input = input()


def isInt(x):
    if int(x) == x:
        return int(x) - 1
    else:
        return int(x)


for i in user_input:
    if i == "[":
        temp += i

result = ""
for i in l:
    if i.isdigit():
        result += str(isInt(float(i)))
        print(result)
    else:
        result += i
print(result)
print(eval(result))
