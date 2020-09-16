import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def horoscope(zodiac):
    if zodiac == 'scorpio':
        zodiac = 'scpo'

    URL = 'https://www.horoscope.com/us/index.aspx'
    driver.get(URL)

    for x in range(5,0,-1):
       results = driver.find_element(By.ID, 'src-hp-'+zodiac[0:x])
       if results is not None:
           break

    results.click()

    driver.implicitly_wait(5)
    page = requests.get(driver.current_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.find('p')

    print(text)

    #driver.find_element(By.XPATH,"//a[@href='" + link + "\"").click()

if __name__ == '__main__':
    zodiac = 'aries'

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=PATH)

    horoscope(zodiac)

    #driver.quit()

