# alpa
# user_input = int(input())
# alpa = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# for i in range(user_input):
#     print(alpa[i] * (i+1))

# array

user_input = int(input())
texts = []
for i in range(user_input):
    texts.append(input())
texts = sorted(texts)
texts = sorted(texts, key=lambda x: len(x))
print(str(texts).replace("'", "").replace("[", "").replace(",", "").replace("]", ""))
