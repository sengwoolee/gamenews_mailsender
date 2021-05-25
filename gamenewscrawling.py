from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 해당 태그를 기다림
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # 태그가 없는 예외 처리
from bs4 import BeautifulSoup
import time

chromedriver = '/usr/local/bin/chromedriver'

options = webdriver.ChromeOptions()
options.add_argument('headless')  # 웹 브라우저를 띄우지 않는 headlss chrome 옵션 적용
options.add_argument('disable-gpu')  # GPU 사용 안함
options.add_argument('lang=ko_KR')  # 언어 설정
driver = webdriver.Chrome(chromedriver, options=options)


class GameNewsCrawling:
    def ruliweb(self):
        print('Ruliweb 뉴스 스크래핑을 시작합니다.')
        url = 'https://bbs.ruliweb.com/news'
        driver.get(url)
        html_dom = driver.page_source
        soup = BeautifulSoup(html_dom, 'html.parser')

        try:  # 정상 처리
            return_data = ['[Ruliweb - 베스트 뉴스]']
            data = soup.select(".bottom_list_item")

            for element in data:
                news_text = element.text
                news_text = news_text.strip()
                news_text = ' '.join(news_text.split())
                return_data.append(news_text)
                return_data.append(element.a['href'])

            print('Ruliweb 뉴스 스크래핑을 완료했습니다.')
            return return_data

        except TimeoutException:  # 예외 처리
            print('해당 페이지에 정보가 존재하지 않습니다.')


    def inven(self):
        print('Inven 뉴스 스크래핑을 시작합니다.')
        url = 'http://www.inven.co.kr/webzine/news/?hotnews=3'
        driver.get(url)
        html_dom = driver.page_source
        soup = BeautifulSoup(html_dom, 'html.parser')

        try:
            return_data = ['[Inven - 인기뉴스]']
            data = soup.select('.content > .title')

            for element in data:
                news_text = element.text
                return_data.append(news_text)
                return_data.append(element.a['href'])

            print('Inven 뉴스 스크래핑을 완료했습니다.')
            return return_data

        except TimeoutException:
            print('해당 페이지에 정보가 존재하지 않습니다.')

    def gamemeca(self):
        print('Gamemeca 뉴스 스크래핑을 시작합니다.')
        url = 'https://www.gamemeca.com/news.php'
        driver.get(url)
        html_dom = driver.page_source
        soup = BeautifulSoup(html_dom, 'html.parser')

        try:
            return_data = ['[Gamemeca - 많이본 뉴스]']
            data = soup.select('.rank_list > ul > li')

            for element in data:
                news_text = element.text
                return_data.append(news_text)
                return_data.append("https://www.gamemeca.com" + element.a['href'])

            print('Gamemeca 뉴스 스크래핑을 완료했습니다.')
            return return_data

        except TimeoutException:
            print('해당 페이지에 정보가 존재하지 않습니다.')

    def igngame(self):
        print('Igngames 뉴스 스크래핑을 시작합니다.')
        url = 'https://www.ign.com/ie?filter=games'
        driver.get(url)
        html_dom = driver.page_source
        soup = BeautifulSoup(html_dom, 'html.parser')

        try:
            return_data = ['[Igngames 뉴스]']
            data = soup.select('.item_title_link')

            for element in data:
                news_text = element.text
                return_data.append(news_text)
                # return_data.append(element.a['href'])

            print('Igngames 뉴스 스크래핑을 완료했습니다.')
            return return_data

        except TimeoutException:
            print('해당 페이지에 정보가 존재하지 않습니다.')
