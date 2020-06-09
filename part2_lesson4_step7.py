from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    book = browser.find_element_by_id("book")
    browser.execute_script("return arguments[0].scrollIntoView(true);", book)

    # Price
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # assert "$100" in price.text

    # Book

    book.click()
    # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()
    x_element = browser.find_element_by_id ("input_value")
    x = x_element.text
    y = calc(x)

    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    input_text = browser.find_element_by_css_selector("#answer")
    input_text.send_keys(y)

    # Отправляем заполненную форму
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()