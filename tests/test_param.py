import pytest
import time
import math
from selenium import webdriver


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_param_link(link):
    driver = webdriver.Chrome()
    driver.get(link)
    driver.implicitly_wait(7)
    answer = str(math.log(int(time.time())))
    print("ОТВЕЕЕТ-----", answer)
    textarea = driver.find_element_by_xpath(
        "//textarea[@placeholder='Напишите ваш ответ здесь...']")
    textarea.send_keys(answer)
    submit = driver.find_element_by_xpath(
        "//button[@class='submit-submission']")
    submit.click()
    feedback_result = driver.find_element_by_xpath(
        "//pre[@class='smart-hints__hint']").text
    print("ОТВЕЕЕТ22222", feedback_result)
    
    feedback_expected = "Correct!"
    assert feedback_expected in feedback_result, "expected '{ }' result '{ }'".format(
        feedback_expected, feedback_result)
    driver.quit()
