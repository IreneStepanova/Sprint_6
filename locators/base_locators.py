from selenium.webdriver.common.by import By


class BaseLocators:
    cookie_button = (By.XPATH, "//button[contains(@class, 'Cookie')]")
    top_order_button = (By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']")
    bottom_order_button = (By.XPATH, "(//button[contains(@class, 'Button_Button') and text()='Заказать'])[last()]")
    scooter_logo = (By.XPATH, "//*[contains(@class, 'Header_LogoScooter')]")
    yandex_logo = (By.XPATH, "//*[contains(@class, 'Header_LogoYandex')]")
