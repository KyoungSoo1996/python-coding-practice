def solution(skill, skill_trees):
    answer = 0
    skillTreeList = list(skill)
    #특수 스킬만 남기기
    for skills in range(len(skill_trees)):
        TempList = []
        for skill in skill_trees[skills]:
            if skill in skillTreeList:
                TempList.append(skill)
        skill_trees[skills] = TempList
    #올바른지 체크
    for skill in skill_trees:
        if skill[:len(skill)] == skillTreeList[:len(skill)]:
            answer +=1
    return answer

testSkill = 'CBD'
testSkill_trees =  ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(testSkill, testSkill_trees))