from selenium import webdriver
import time
import math
import os



try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_name("firstname").send_keys("1")
    browser.find_element_by_name("lastname").send_keys("1")
    browser.find_element_by_name("email").send_keys("1")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '1.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_name("file").send_keys(file_path)
    # Отправляем заполненную форму

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
