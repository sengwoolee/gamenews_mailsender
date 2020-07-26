# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from gamenewscrawling import GameNewsCrawling
import datetime


class MailSender:
    game_news_crawling = GameNewsCrawling()
    ruliweb_news = game_news_crawling.ruliweb()
    inven_news = game_news_crawling.inven()

    ruliweb_newsmsg = "\n".join(ruliweb_news) + "\n"
    inven_newsmsg = "\n".join(inven_news) + "\n"

    news_msg = ruliweb_newsmsg + "\n" + inven_newsmsg

    nowDatetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M') # 2020-07-25 15:21

    msg = MIMEText(news_msg)
    msg['Subject'] = Header(nowDatetime + ' 게임뉴스', 'utf-8')
    msg['From'] = 'leesengwoo555@gmail.com'
    msg['To'] = 'leesengwoo555@gmail.com'

    with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
        smtp.login('leesengwoo555@gmail.com', 'apppassword')
        smtp.send_message(msg)
        smtp.quit()
