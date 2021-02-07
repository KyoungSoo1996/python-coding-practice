# 아이디 길이는 3자 이상 15자 이하
# 아이디는 알파벳 소문자, 숫자, -, _, . 문자만 사용할 수 있다.
# .는 처음과 끝에 사용할 수 없고, 연속으로 사용할 수 없다.

# 1. new_id의 모든 대문자를 대응되는 소문자로 치환
# 2. new_id에서 알파벳, 소문자, 숫자, 특수문자를 제외한 모든 문자는 제거함
# 3. .가 2번 이상이면 하나의 .으로 치환
# 4. new_id에 .이 처음과 끝에 있으면 제거
# 5. new_id가 빈문자열이면 new_id에 a를 대입한다.
# 6. new_id 길이가 16자 이상이면 15개의 문자를 제외한 나머지 문자를 제거 제거후에 .이면 .제거
# 7. new_id의 길이가 2자 이하이면 마지막 문자를 3이 될때까지 붙인다.

import re


def solution(new_id):
    answer = ''
    # 1번 규칙
    new_id = new_id.lower()
    # 2번 규칙
    for word in new_id:
        if word.isnumeric() or word.islower(
        ) or word == '.' or word == '_' or word == '-':
            answer += word

    # 3번 규칙
    answer = re.sub('\.+', '.', answer)

    # 4번 규칙
    if answer != '':
        if answer[0] == '.':
            answer = answer[1:]

    if answer != '':
        if answer[-1] == '.':
            answer = answer[:-1]

    # 5번 규칙
    if answer == '':
        answer += 'a'

    # 6번 규칙
    if len(answer) >= 16:
        answer = answer[:15]

    # 7번 규칙
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    # 4번 규칙
    if answer != '':
        if answer[0] == '.':
            answer = answer[1:]

    if answer != '':
        if answer[-1] == '.':
            answer = answer[:-1]

    return answer


print(solution(data))