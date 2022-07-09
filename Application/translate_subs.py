from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchFrameException
from bs4 import BeautifulSoup
from time import sleep
from tkinter import *
from paste_from_clipboard import *
from time import sleep
def translate_text(text_to_translate):
    browser = Chrome(r"C:\Users\Никита\Desktop\chromedriver.exe")
    url = "https://translate.google.com/"

    browser.get(url)
    input_tab = browser.find_element(By.CLASS_NAME, "er8xn")
    input_tab.send_keys(str(text_to_translate))

    sleep(3)
    output_tab = browser.find_elements(By.CLASS_NAME, "Q4iAWc")


    print(output_tab[0].text)

    return str(output_tab[0].text)


