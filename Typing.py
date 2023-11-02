import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui

browser = webdriver.Chrome()

url ="https://humanbenchmark.com/tests/typing"
browser.get(url)

page_source = browser.page_source

soup = BeautifulSoup(page_source,'html.parser')
spans = soup.find_all('span', class_='incomplete')
text = ''.join([span.get_text() for span in spans])
print(text)

time.sleep(2)

pyautogui.write(text,interval=0)

time.sleep(10000)