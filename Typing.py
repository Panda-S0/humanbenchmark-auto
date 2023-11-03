#import needed libraries
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui

#opens a browser with that url
browser = webdriver.Chrome()
url ="https://humanbenchmark.com/tests/typing"
browser.get(url)

#get the html source file or something
page_source = browser.page_source

#get the text to be written
soup = BeautifulSoup(page_source,'html.parser')
spans = soup.find_all('span', class_='incomplete')
text = ''.join([span.get_text() for span in spans])

time.sleep(2)

#write the text
pyautogui.write(text,interval=0)

#wait
time.sleep(10000)