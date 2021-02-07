user_Num = input()
user_height = input()
l = user_height.split(" ")
result = 0
for i in range(0, int(user_Num)):
    if float(l[i]) >= 3:
        result = i
        break
print(int(user_Num) - result)
