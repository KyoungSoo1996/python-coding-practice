def solution(phone_book):
    answer = True
    phone_book =  sorted(phone_book)
    for i in range(1,len(phone_book)):
        if phone_book[i].find(str(phone_book[0])) != -1:
            answer = False
            break
    return answer

def best_solution(phoneBook):
    phoneBook = sorted(phoneBook)
    
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True



testPhone = ['119', '97674223', '1295524421']
testPhone2 = ['123','456','789']
print(solution(testPhone2))
print(best_solution(testPhone2))
