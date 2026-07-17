import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Кликнуть на вопрос номер {question_number}")
    def click_question(self, question_number):
        locator = (MainPageLocators.question[0], MainPageLocators.question[1].format(question_number))
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текст ответа на вопрос номер {question_number}")
    def get_answer_text(self, question_number):
        locator = (MainPageLocators.answer[0], MainPageLocators.answer[1].format(question_number))
        return self.get_text_from_element(locator)
