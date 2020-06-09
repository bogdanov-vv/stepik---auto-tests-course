from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Page 1
    # button1 = browser.find_element_by_class_name("trollface.btn.btn-primary")
    # button1.click()

    # Next tab
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)

    # Ваш код, который заполняет обязательные поля
    # x_element = browser.find_element_by_id("input_value")
    # x = x_element.text
    # y = calc(x)
    # field = browser.find_element_by_css_selector("#answer")
    # field.send_keys(y)

    # Price
    price = WebDriverWait(browser, 12).until(EC.element_to_be_selected(By.ID, "price"))
    price_text = price.text
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()