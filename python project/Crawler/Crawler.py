import time
import sys
from bs4 import BeautifulSoup
from selenium import webdriver

query_txt = input("크롤링 키워드는?: ")
path = 'E:/python project/Crawler/' #텍스트를 저장할 위치
f_name = path + query_txt + '.txt'

path = 'E:/chromedriver2.40/chromedriver_win32/chromedriver.exe' #크롬 드라이버가 있는 위치
driver = webdriver.Chrome(path) #크롬 웹드라이버 등록
driver.get("https://korean.visitkorea.or.kr/main/main.html")
time.sleep(2)

driver.find_element_by_id("btnSearch").click() #검색 버튼 클릭
element = driver.find_element_by_id("inp_search") #검색창 확보
element.send_keys(query_txt) #검색창에 검색어 전송

driver.find_element_by_link_text("검색").click() #검색 후 연결된 페이지로 이동

time.sleep(1)
full_html = driver.page_source #검색된 페이지 전체 확보
soup = BeautifulSoup(full_html, 'html.parser') #확보된 페이지에서 HTML 분석
content_list = soup.find('ul', class_ = "list_thumType flnon") #list_thumType flnon 부분 추출

for i in content_list: #출력
    print(i.text.strip())
    print('\n')

f = open(f_name, 'w', encoding='UTF-8')
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
content_list = soup.find('ul', class_ = 'list_thumType flnon')

for i in content_list: #파일에 쓰기
    f.write(i.text.strip()+'\n\n')

f.close()
print("Finish Crawler!!!")
