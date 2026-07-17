import allure
from data.urls import BASE_URL, DZEN_URL
from pages.main_page import MainPage


@allure.feature("Логотипы")
class TestLogo:

    @allure.title("Проверка перехода на главную по клику на лого Самоката")
    @allure.description("Нажать на лого Самоката — должен быть редирект на главную страницу")
    @allure.severity(allure.severity_level.NORMAL)
    def test_scooter_logo_redirect(self, driver):
        with allure.step("Перейти на страницу заказа и кликнуть логотип Самоката"):
            main_page = MainPage(driver)
            main_page.accept_cookies()
            main_page.click_top_order_button()
            main_page.click_scooter_logo()

        with allure.step("Проверить, что вернулись на главную страницу"):
            assert main_page.get_current_url() == BASE_URL

    @allure.title("Проверка открытия Дзена по клику на лого Яндекса")
    @allure.description("Нажать на лого Яндекса — в новом окне должен открыться Дзен")
    @allure.severity(allure.severity_level.NORMAL)
    def test_yandex_logo_redirect(self, driver):
        with allure.step("Кликнуть логотип Яндекса"):
            main_page = MainPage(driver)
            main_page.accept_cookies()
            main_page.click_yandex_logo()

        with allure.step("Переключиться на новое окно"):
            main_page.switch_to_new_window()

        with allure.step("Проверить, что URL содержит dzen.ru"):
            main_page.wait_for_url_contains(DZEN_URL)
            assert DZEN_URL in main_page.get_current_url()
