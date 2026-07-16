import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
            current_url = driver.current_url
            assert current_url == BASE_URL

    @allure.title("Проверка открытия Дзена по клику на лого Яндекса")
    @allure.description("Нажать на лого Яндекса — в новом окне должен открыться Дзен")
    @allure.severity(allure.severity_level.NORMAL)
    def test_yandex_logo_redirect(self, driver):
        with allure.step("Кликнуть логотип Яндекса"):
            main_page = MainPage(driver)
            main_page.accept_cookies()
            original_window = driver.current_window_handle
            main_page.click_yandex_logo()

        with allure.step("Переключиться на новое окно"):
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            all_windows = driver.window_handles
            new_window = [w for w in all_windows if w != original_window][0]
            driver.switch_to.window(new_window)

        with allure.step("Проверить, что URL содержит dzen.ru"):
            WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
            current_url = driver.current_url
            assert DZEN_URL in current_url
