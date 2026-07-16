import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_locators import BaseLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент с ожиданием")
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Дождаться видимости элемента")
    def wait_for_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Прокрутить к элементу и кликнуть")
    def scroll_and_click(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(0.3)
        element.click()

    @allure.step("Ввести текст в элемент")
    def send_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получить текст из элемента")
    def get_text_from_element(self, locator):
        element = self.wait_for_visibility(locator)
        return element.text

    @allure.step("Принять куки")
    def accept_cookies(self):
        self.click_on_element(BaseLocators.cookie_button)

    @allure.step("Нажать верхнюю кнопку Заказать")
    def click_top_order_button(self):
        self.scroll_and_click(BaseLocators.top_order_button)

    @allure.step("Нажать нижнюю кнопку Заказать")
    def click_bottom_order_button(self):
        self.scroll_and_click(BaseLocators.bottom_order_button)

    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click_on_element(BaseLocators.scooter_logo)

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_on_element(BaseLocators.yandex_logo)
