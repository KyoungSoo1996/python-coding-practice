import math

user_input = input()
user_num = input()
bro = []
for i in range(2):
    bro.append(int(user_input.split(" ")[i]))

for i in range(int(user_num)):
    if i % 2 == 0:
        temp = math.ceil(bro[0] / 2)
        bro[1] = bro[1] + temp
        bro[0] = bro[0] - temp
    else:
        temp = math.ceil(bro[1] / 2)
        bro[0] = bro[0] + temp
        bro[1] = bro[1] - temp
print(str(bro[0]) + " " + str(bro[1]))
