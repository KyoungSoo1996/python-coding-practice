#English Vowel : [a,e,i,o,u]


def PartialStringReverse(s):
    Vowels = ['a', 'e', 'i', 'o', 'u']
    Vowels += list(''.join(Vowels).upper())

    result = list(s)
    usingVowels = []

    for index, word in enumerate(s):
        if word in Vowels:
            usingVowels.append(word)
            result[index] = ''

    for num in range(len(result)):
        if result[num] == '':
            result[num] = usingVowels.pop()

    return ''.join(result)

목적. 영어의 모음만 골라 뒤집어서 문자열을 만들어라.
1. 모음 리스트를 만든다. + 소문자만 나온다는 조건이 없기 때문에, 대문자도 리스트에 추가한다.
2. 결과를 담을 상자와 사용한 모음이 담길 상자를 만든다.
3. 모음이 들어간 문자열 위치에 공백을 넣고, 사용한 모음을 상자에 넣는다.
4. 공백이 있는 위치에 끝에서부터 하나씩 사용한 모음을 붙인다.
5. 나온 결과값을 string으로 변환한다.


print(PartialStringReverse('kongstudios'))
