from selenium import webdriver
import time
import math

from selenium.webdriver.support.select import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()
    browser.switch_to.alert.accept()

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_id("input_value")
    x = input1.text

    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)
    # Отправляем заполненную форму
    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
