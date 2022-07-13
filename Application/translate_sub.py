from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
def translate_text(text_to_translate):
    browser = Chrome(r"C:\Users\Никита\Desktop\chromedriver.exe")
    url = "https://translate.google.com/"
    browser.get(url)
    input_tab = browser.find_element(By.CLASS_NAME, "er8xn")
    #sends data
    input_tab.send_keys(str(text_to_translate))
    #programm needs some time to download web page and get data
    sleep(3)
    output_tab = browser.find_elements(By.CLASS_NAME, "Q4iAWc")
    print(output_tab[0].text)
    return str(output_tab[0].text)
