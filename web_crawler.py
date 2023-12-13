import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def simple_web_crawler():
    # 爬蟲測試程式
    url = 'https://alternative.me/crypto/fear-and-greed-index/'  # 要爬取的網站 URL
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('成功取得網頁內容：')
            print(response.text)  # 將網頁內容列印出來
        else:
            print(f'取得網頁內容失敗，狀態碼：{response.status_code}')
    except requests.RequestException as e:
        print(f'發生錯誤：{e}')

def headless_web_crawler():
    # 使用 Chrome headless 模式的爬蟲程式
    url = 'https://alternative.me/crypto/fear-and-greed-index/'  # 要爬取的網站 URL

    options = Options()
    options.add_argument('--headless')  # 設定為 headless 模式
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        print('成功取得網頁內容（headless 模式）：')
        print(driver.page_source)  # 取得網頁內容
    finally:
        driver.quit()

def beautifulsoup_web_crawler():
    # 使用 BeautifulSoup 解析網頁內容的爬蟲程式
    url = 'https://www.istock.tw/post/twmarginrequirement'  # 要爬取的網站 URL

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # 在這裡使用 BeautifulSoup 解析網頁內容
            print('成功取得網頁內容（BeautifulSoup）：')
            print(soup.title)  # 以範例方式列印出網頁的標題
        else:
            print(f'取得網頁內容失敗，狀態碼：{response.status_code}')
    except requests.RequestException as e:
        print(f'發生錯誤：{e}')

if __name__ == "__main__":
    simple_web_crawler()  # 執行基本爬蟲程式
    headless_web_crawler()  # 執行 headless 爬蟲程式
    beautifulsoup_web_crawler()  # 執行 BeautifulSoup 爬蟲程式
