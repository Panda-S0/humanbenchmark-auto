import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui

words=[' ']
browser = webdriver.Chrome()

url ="https://humanbenchmark.com/tests/verbal-memory"
browser.get(url)

time.sleep(5)

def get_word():
    page_source = browser.page_source
    soup = BeautifulSoup(page_source,'html.parser')
    spans = soup.find_all('div', class_='word')
    text = ''.join([span.get_text() for span in spans])
    return text

def press(SN):
    #s666888
    #n888888
    if SN =='S':
        # print('SEEN')
        pyautogui.click(666,888)
    elif SN =='N':
        # print('NEW')
        pyautogui.click(888,888)


def main():

    while True:
        print(words)
        word=get_word()

        for i in range(len(words)):
            # print(i,len(words))
            if word == words[i]:
                # print(words[i],' ',word)
                press('S')
                break
            elif i == len(words)-1:
                words.append(word)
                press('N')


main()
