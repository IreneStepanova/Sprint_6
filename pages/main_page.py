import time

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Кликнуть на вопрос номер {question_number}")
    def click_question(self, question_number):
        locator = (By.ID, MainPageLocators.question[1].format(question_number))
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(0.3)
        self.click_on_element(locator)

    @allure.step("Получить текст ответа на вопрос номер {question_number}")
    def get_answer_text(self, question_number):
        locator = (By.ID, MainPageLocators.answer[1].format(question_number))
        return self.get_text_from_element(locator)
