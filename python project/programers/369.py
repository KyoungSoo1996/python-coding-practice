# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
result = 0
for i in range(1, int(user_input) + 1):
    for k in range(len(str(i))):
        if str(i)[k] == "3" or str(i)[k] == "6" or str(i)[k] == "9":
            print(i)
            result += 1

print(result)
