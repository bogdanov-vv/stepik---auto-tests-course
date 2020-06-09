from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    num = browser.find_element_by_css_selector("#num1")
    num_val = num.text

    num2 = browser.find_element_by_css_selector("#num2")
    num2_val = num2.text

    y = int(num_val) + int(num2_val)
    print(y)

    # browser.find_element_by_css_selector("#dropdown").click()
    # browser.find_element_by_css_selector()



    # select = Select(browser.find_element_by_css_selector("#dropdown"))
    # select.select_by_value(y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(y))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
