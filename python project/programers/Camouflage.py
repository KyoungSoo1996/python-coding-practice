
def solution(clothes):
    clotheKind ={}
    prct = 1
    #list up
    for i in clothes:
        if i[1] not in clotheKind:
            clotheKind.setdefault(i[1], 1)
        else :
            clotheKind[i[1]] += 1

    #product
    for i in clotheKind.values():
        prct = prct *(i+1)
    prct -= 1
    return prct

testClothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]

print(solution(testClothes))

