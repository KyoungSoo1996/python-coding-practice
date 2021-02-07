def solution(numbers, hand):
    answer = ''
    lefthand = 10
    righthand = 12

    for number in numbers:
        if number == 0:
            number = 11
        if number in [1, 4, 7]:
            lefthand = number
            answer += 'L'
        elif number in [3, 6, 9]:
            righthand = number
            answer += 'R'
        else:
            right = handLength(righthand, number)
            left = handLength(lefthand, number)
            if right > left:
                answer += 'L'
                lefthand = number
            elif right < left:
                answer += 'R'
                righthand = number
            else:
                if hand == 'right':
                    answer += 'R'
                    righthand = number
                else:
                    answer += 'L'
                    lefthand = number
    return answer


def handLength(current, pos):
    length = 0
    while pos != current:
        if pos > current:
            if pos >= current + 3:
                current = current + 3
                length += 1
            elif pos >= current + 1:
                current = current + 1
                length += 1

        else:
            if pos <= current - 3:
                current = current - 3
                length += 1
            elif pos <= current - 1:
                current = current - 1
                length += 1
    return (length)


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
