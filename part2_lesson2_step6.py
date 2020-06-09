from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение для переменной х
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text

    # Считаем функцию
    y = calc(x)

    # Скролим страницу вниз
    input_field = browser.find_element_by_css_selector('#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
    input_field.send_keys(y)

    # Чекбокс
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()

    # Радиокнопка
    radio = browser.find_element_by_css_selector("#robotsRule")
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
