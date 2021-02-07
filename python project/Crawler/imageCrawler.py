import time
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request

pageNum = 100
artworkCount = 0
artworkURLs = []
artworkNs = []
artworkUNs = []

path = 'E:/chromedriver2.40/chromedriver_win32/chromedriver.exe'  # 크롬 드라이버가 있는 위치
driver = webdriver.Chrome(path)  # 크롬 웹드라이버 등록

for index in range(81, pageNum):

    #이미지 URL 받아오기
    driver.get("https://artisty.co.kr/shop.html?p=" + str(index))
    full_html = driver.page_source  # 검색된 페이지 전체 확보
    soupURL = BeautifulSoup(full_html, 'html.parser')  # 확보된 페이지에서 HTML 분석
    soup = soupURL.find('div', class_='wrapper')
    imgURLs = soup.find_all('img', class_='item-thumb abs-center')
    for imgurl in imgURLs:
        artworkURLs.append('https://artisty.co.kr/' + str(str(imgurl).split("src=")
                                                          [1]).replace('\"', '').replace('/>', ''))
        artworkCount += 1

    # 작가명 가져오기
    names = soup.find_all('small', class_='text-smaller')
    for name in names:
        temp = str(name).split("> ")[1].replace(
            '</small>', '').replace('/', '')
        temp = temp.replace(':', '').replace('|', '')
        temp = temp.replace('?', '')
        artworkUNs.append(temp)

    # 작품명 가져오기
    artworkNames = soup.find_all('a', class_='art-item-link')
    for artwork in artworkNames:
        temp = str(artwork).split('>')[1].replace('</a', '').replace('/', '')
        temp = temp.replace(':', '').replace('|', '')
        temp = temp.replace('?', '')
        artworkNs.append(temp)

    #이미지를 저장하되 "작품명[작가명]" 으로 파일명을 만들기
    for i in range(1, artworkCount):
        urllib.request.urlretrieve(
            artworkURLs[i], 'img/' + artworkNs[i]+' [' + artworkUNs[i] + '].jpg')
