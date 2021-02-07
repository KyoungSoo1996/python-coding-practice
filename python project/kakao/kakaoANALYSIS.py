#파일을 가져왔다
dataPath = 'E:/python project/kakao/KakaoTalk_20200901_0258_41_226_group.txt'
f_name = dataPath
open_file = open(f_name, encoding="utf8")

#csv 형식으로 바꿔봤다.
changeData =''
changeData = str(open_file.readlines())

changeData = changeData.replace('\\n',',')
changeData =changeData.replace(':',',')
#리스트에 넣는다.
temp = changeData.split(',')
#4번까지 필요없는 정보
worddata = []#대화 내용을 넣을 것
for i in range(len(temp)):
    worddata.append(temp[i])

#가장 말이 많은 사람 찾기

nameTag = [' 퉤 ', ' 부끄롱 ',' 케케 ',' 욕쟁이 ', ' 을유 ', ' 꾬 ']
tomuchSpeaker =[]
for i in nameTag:
    tomuchSpeaker.append(i +'(이)가 말한 횟수 : '+ str(worddata.count(i)))
print(tomuchSpeaker)

#이름 지우기
for i in worddata:
    if i in nameTag:
        worddata.remove(i)


#형태소 분석기를 가져와 시작하기
import rhinoMorph
from collections import Counter
rn = rhinoMorph.startRhino()

#형태소 분석하기
wordAnalysis = []
result = []
p =[]
for i in worddata:
    wordAnalysis.append(rhinoMorph.onlyMorph_list(rn, i, pos=['NNG', 'NNP','NNB','NP']))
    for j in wordAnalysis:
       if len(j) >0:
           for n in j:
               result.append(n)

    wordAnalysis =[]

#빈도가 얼마나 되는지 검색하기
result = Counter(result)

#파일로 저장하기
savepath = 'E:/python project/KAKAO/'
save_file = savepath + 'result.txt'
save = open(save_file, 'w', encoding='UTF-8')

save.write(str(result))

save.close()
print("Finish!!!")