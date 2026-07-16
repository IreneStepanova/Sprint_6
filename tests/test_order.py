import allure
import pytest
from data.test_data import first_order, second_order
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Оформление заказа через верхнюю кнопку Заказать")
    @allure.description("Позитивный сценарий: нажать верхнюю кнопку, заполнить форму, подтвердить заказ")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_order_from_top_button(self, driver):
        with allure.step("Нажать кнопку Заказать вверху страницы"):
            main_page = MainPage(driver)
            main_page.accept_cookies()
            main_page.click_top_order_button()

        with allure.step("Заполнить форму заказа первым набором данных"):
            order_page = OrderPage(driver)
            order_page.fill_first_form(
                first_order[0], first_order[1], first_order[2],
                first_order[3], first_order[4]
            )
            order_page.fill_second_form(
                first_order[5], first_order[6], first_order[7], first_order[8]
            )
            order_page.submit_order()
            order_page.confirm_order()

        with allure.step("Проверить, что появилось сообщение об успешном создании заказа"):
            success_text = order_page.get_success_message_text()
            assert "Заказ оформлен" in success_text

    @allure.title("Оформление заказа через нижнюю кнопку Заказать")
    @allure.description("Позитивный сценарий: нажать нижнюю кнопку, заполнить форму, подтвердить заказ")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_order_from_bottom_button(self, driver):
        with allure.step("Нажать кнопку Заказать внизу страницы"):
            main_page = MainPage(driver)
            main_page.accept_cookies()
            main_page.click_bottom_order_button()

        with allure.step("Заполнить форму заказа вторым набором данных"):
            order_page = OrderPage(driver)
            order_page.fill_first_form(
                second_order[0], second_order[1], second_order[2],
                second_order[3], second_order[4]
            )
            order_page.fill_second_form(
                second_order[5], second_order[6], second_order[7], second_order[8]
            )
            order_page.submit_order()
            order_page.confirm_order()

        with allure.step("Проверить, что появилось сообщение об успешном создании заказа"):
            success_text = order_page.get_success_message_text()
            assert "Заказ оформлен" in success_text
