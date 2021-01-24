from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import math
import unittest
import time


class TestFirst(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath(
            '//input[contains(@placeholder, "first")]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath(
            '//input[contains(@placeholder, "last")]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath(
            '//input[contains(@placeholder, "email")]')
        input3.send_keys("email@test.com")
        input4 = browser.find_element_by_xpath(
            '//input[contains(@placeholder, "phone")]')
        input4.send_keys("9163378875")
        input5 = browser.find_element_by_xpath(
            '//input[contains(@placeholder, "address:")]')
        input5.send_keys("russia,moscow")
        button = browser.find_element_by_xpath('//*[@type ="submit"]')
        time.sleep(5)
        button.click()
        time.sleep(5)
        expected_result = "Congratulations! You have successfully registered!"
        actual_result = browser.find_element_by_tag_name('h1').text
        # assert expected_result in actual_result, "expected_result '{expected_result}', got '{actual_result}'"
        self.assertEqual(expected_result, actual_result,
                         "ОШИБКА")
        time.sleep(2)
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath(
            '//input[contains(@placeholder, "first")]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath(
            '//input[contains(@placeholder, "last")]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath(
            '//input[contains(@placeholder, "email")]')
        input3.send_keys("email@test.com")
        input4 = browser.find_element_by_xpath(
            '//input[contains(@placeholder, "phone")]')
        input4.send_keys("9163378875")
        input5 = browser.find_element_by_xpath(
            '//input[contains(@placeholder, "address:")]')
        input5.send_keys("russia,moscow")
        button = browser.find_element_by_xpath('//*[@type ="submit"]')
        time.sleep(5)
        button.click()
        time.sleep(5)
        expected_result = "Congratulations! You have successfully registered!"
        actual_result = browser.find_element_by_tag_name('h1').text
        # assert expected_result in actual_result, "expected_result '{expected_result}', got '{actual_result}'"
        self.assertEqual(expected_result, actual_result,
                         "ОШИБКА")
        time.sleep(2)

        browser.quit()


if __name__ == "__main__":
    unittest.main()
