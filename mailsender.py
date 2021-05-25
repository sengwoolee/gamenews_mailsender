# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from gamenewscrawling import GameNewsCrawling
import datetime


class MailSender:
    sendemail = input('발송할 이메일을 입력해주세요.')
    apppassword = input('앱 패스워드를 입력해주세요.')
    toemail = input('수신할 이메일을 입력해주세요.')

    game_news_crawling = GameNewsCrawling()
    ruliweb_news = game_news_crawling.ruliweb()
    inven_news = game_news_crawling.inven()
    gamemeca_news = game_news_crawling.gamemeca()
    igngames_news = game_news_crawling.igngame()

    ruliweb_newsmsg = "\n".join(ruliweb_news) + "\n"
    inven_newsmsg = "\n".join(inven_news) + "\n"
    gamemeca_newsmsg = "\n".join(gamemeca_news) + "\n"
    igngames_newsmsg = "\n".join(igngames_news) + "\n"

    news_msg = ruliweb_newsmsg + "\n" + inven_newsmsg + "\n" + gamemeca_newsmsg + "\n" + igngames_newsmsg

    nowDatetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M') # 2020-07-25 15:21

    msg = MIMEText(news_msg)
    msg['Subject'] = Header(nowDatetime + ' 게임뉴스', 'utf-8')
    msg['From'] = sendemail
    msg['To'] = toemail

    with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
        smtp.login(sendemail, apppassword)
        smtp.send_message(msg)
        smtp.quit()
        
    print('스크래핑된 뉴스를 메일로 발송했습니다.')
