#1. 날짜 입력받아 판별하기
# date = input('DD MTH YYYY 형식으로 날짜를 입력하세요: ')
# print('Jan' in date)

#2. 산성도 입력받아 판별하기
# ph = float(input('PH 농도를 입력하세요 : '))
# if ph < 7.0:
#     print(ph, "은(는) 산성입니다.")
# else:
#     print(ph, "은(는) 염기성입니다.")

compound = input('분자를 입력하세요 : ')
if compound == "H2O":
    print("물")
elif compound == "NH3":
    print("암모니아")
elif compound == "CH4":
    print("메탄")
else:
    print("알 수 없음")