from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    img = browser.find_element_by_css_selector("#treasure")
    img_val = img.get_attribute("valuex")

    # x_element = browser.find_element_by_id ("input_value")
    # x = x_element.text
    # y = calc(x)
    y = calc(img_val)
    input_text = browser.find_element_by_css_selector("#answer")
    input_text.send_keys(y)
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
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
