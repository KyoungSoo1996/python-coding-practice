from random import randint


def makeFunData(a, b, frequency, file):
    for i in range(frequency):
        ran = randint(1, 1000)
        file.write(str(ran) + "," + str(a + b * ran))
        file.write("\n")
    print("Data Making End")


fin = open("data.csv", "w", encoding="utf8")


makeFunData(5, 10, 100, fin)
