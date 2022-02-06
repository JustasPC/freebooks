from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Firefox()

browser.get('https://all-ebook.info/')

listas = []


def search():
    browser.get('https://all-ebook.info/')
    global listas
    el = browser.find_elements_by_class_name('mov-t')
    url=[]
    for i in el:
        url.append([i.get_attribute('href'),i.text])
    for i in url:
        href = i[0].split('https://all-ebook.info/')[1].split('.html')[0]
        if not(href in listas):
            print(i)
            f = open("log.txt", "a")
            listas.append(href)
            f.write(i[1])
            f.write(' ')
            f.write(';')
            f.write(i[0])
            f.write(' ')
            f.write(';')
            f.write(href)
            f.write('\n')
            f.close()
            browser.get(i[0])
            browser.get_full_page_screenshot_as_file(href+'.png')

def fix_file_name(i):
    href = i.get_attribute('href').split('https://all-ebook.info/')[1].split('.html')[0]
    return href


while True:
    search()
