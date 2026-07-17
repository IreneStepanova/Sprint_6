import allure
import pytest
from data.test_data import question_answers
from pages.main_page import MainPage


@allure.feature("Раздел «Вопросы о важном»")
class TestFAQ:

    @allure.title("Проверка текста ответа на вопрос")
    @allure.description("Нажимаем на вопрос в аккордеоне и проверяем, что открылся правильный текст ответа")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("question_number, expected_answer", question_answers)
    def test_faq_answer_text(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_question(question_number)
        actual_answer = main_page.get_answer_text(question_number)
        with allure.step("Проверить, что текст ответа совпадает с ожидаемым"):
            assert actual_answer == expected_answer
