# 코딩테스트 참여 언어는 cpp, java, python 중 하나를 선택해야함
# 지원 직군은 backend와 frontend 중 하나를 선택해야함
# 지원 경력 구분에 junior와 senior 중 하나를 선택해야함
# 선호 푸드로 chicken과 pizza중 하나를 선택해야함

# 위의 4가지 정보와 획득한 코딩테스트 점수를 적은 하나의 문자열로
# 해당하는 사람들의 숫자를 순서대로 배열에 담아 return



def solution(info, query):
    for num in range(len(query)):
        query[num] = query[num].replace(' and', '')

    filterLanage = ['cpp', 'java', 'python', '-']
    filterWork = ['backend', 'frontend', '-']
    filterLength = ['junior', 'senior', '-']
    filterfood = ['chicken', 'pizza', '-']

    people = [[] for i in range(len(info))]
    querys = [[] for i in range(len(query))]
    #data array
    for i in range(len(info)):
        index = 0
        for code in info[i].split():
            if index == 0:
                people[i].append(filterLanage.index(str(code)))
                index += 1
            elif index == 1:
                people[i].append(filterWork.index(str(code)))
                index += 1
            elif index == 2:
                people[i].append(filterLength.index(str(code)))
                index += 1
            elif index == 3:
                people[i].append(filterfood.index(str(code)))
                index += 1
            elif index == 4:
                people[i].append(int(code))
                index += 1
    for i in range(len(query)):
        index = 0
        for code in query[i].split():
            if index == 0:
                querys[i].append(filterLanage.index(str(code)))
                index += 1
            elif index == 1:
                querys[i].append(filterWork.index(str(code)))
                index += 1
            elif index == 2:
                querys[i].append(filterLength.index(str(code)))
                index += 1
            elif index == 3:
                querys[i].append(filterfood.index(str(code)))
                index += 1
            elif index == 4:
                querys[i].append(int(code))
                index += 1

    answer = []
    for condition in querys:
        answer.append(
            len(
                list(
                    filter(
                        lambda x:
                        (condition[0] == 3 or x[0] in [condition[0], 3]) and
                        (condition[1] == 2 or x[1] in [condition[1], 2]) and
                        (condition[2] == 2 or x[2] in [condition[2], 2]) and
                        (condition[3] == 2 or x[3] in [condition[3], 2]) and x[
                            4] >= condition[4], people))))
    return answer


print(solution(info, query))