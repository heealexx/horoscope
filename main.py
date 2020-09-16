import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def horoscope(zodiac):
    sign = {"aries":"1", "taurus":"2", "gemini":"3", "cancer":"4", "leo":"5", "virgo":"6",
            "libra":"7", "scorpio":"8", "sagittarius":"9", "capricorn":"10", "aquarius":"11", "pisces":"12"}
    value = sign[zodiac]
    URL = 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign='+value

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.find('p').get_text()

    print('horoscope.com: '+text)

def astrology(zodiac):
    URL = 'https://www.astrology.com/horoscope/daily/'+zodiac+'.html'

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    text = soup.find('p').get_text()
    print('astrology.com: '+text)

def astrostyle(zodiac):
    URL = 'https://astrostyle.com/horoscopes/daily/'+zodiac+'/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.find('div', class_ = 'horoscope-content')
    text2 = text.find('p').get_text()
    print('astrostyle.com: '+text2)

if __name__ == '__main__':
    print('Enter your zodiac sign for your daily dose of horoscope!')
    zodiac = input()

    horoscope(zodiac)
    astrology(zodiac)
    astrostyle(zodiac)
