import pytest
from selenium import webdriver
import time
import math

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestMainPage1():
    final = ''
    @pytest.mark.parametrize('url', ['https://stepik.org/lesson/236895/step/1',
                                     'https://stepik.org/lesson/236896/step/1',
                                     'https://stepik.org/lesson/236897/step/1',
                                     'https://stepik.org/lesson/236898/step/1',
                                     'https://stepik.org/lesson/236899/step/1',
                                     'https://stepik.org/lesson/236903/step/1',
                                     'https://stepik.org/lesson/236904/step/1',
                                     'https://stepik.org/lesson/236905/step/1'])
    def test(self, url):
        browser = webdriver.Chrome()
        result_str = ''
        try:
            browser.get(url)
            answer = math.log(int(time.time()))
            WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
            browser.find_element_by_tag_name("textarea").send_keys(str(answer))
            browser.find_element_by_class_name("submit-submission").click()
            result = WebDriverWait(browser, 15).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "smart-hints__hint")))
            if result.text != "Correct!":
                result_str += result.text

            print(result_str)
        finally:
            browser.quit()
