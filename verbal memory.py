#import needed libraries
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui

#set an empty array to store words
words=[' ']

#opens a browser with that url
browser = webdriver.Chrome()
url ="https://humanbenchmark.com/tests/verbal-memory"
browser.get(url)

time.sleep(5)

#getting the current word by finding the dic called word
def get_word():
    page_source = browser.page_source
    soup = BeautifulSoup(page_source,'html.parser')
    spans = soup.find_all('div', class_='word')
    text = ''.join([span.get_text() for span in spans])
    return text

#press on seen when the word is seen and new when its new
def press(SN):
    if SN =='S':
        pyautogui.click(666,888)
    elif SN =='N':
        pyautogui.click(888,888)


def main():

    while True:
        word=get_word()

        #check if the word is in the list and tell press function
        for i in range(len(words)):
            if word == words[i]:
                press('S')
                break
            elif i == len(words)-1:
                words.append(word)
                press('N')

#run main function
main()
