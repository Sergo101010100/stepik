import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = " http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    browser.find_element_by_id("book").click()

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_id("input_value")
    x = input1.text

    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)
    # Отправляем заполненную форму
    button1 = browser.find_element_by_id("solve")
    button1.click()

    browser.switch_to.alert

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
