from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first = browser.find_element_by_css_selector("input[placeholder='Enter first name']")
    first.send_keys('First')
    second = browser.find_element_by_css_selector("input[placeholder='Enter last name']")
    second.send_keys('Second')
    third = browser.find_element_by_css_selector("input[placeholder='Enter email']")
    third.send_keys('test@mail.com')


    # загружаем файл
    element = browser.find_element_by_css_selector("input[name='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()