user_input = input()
l = user_input.split(" ")
result = ""
for i in range(int(l[0]), int(l[1]) + 1):
    if i % 5 == 0:
        result += " " + str(i)
print(result[1:])
