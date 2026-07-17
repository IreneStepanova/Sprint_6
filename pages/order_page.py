import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Заполнить первую часть формы: {first_name} {last_name}, {address}, {metro}, {phone}")
    def fill_first_form(self, first_name, last_name, address, metro, phone):
        self.send_text_to_element(OrderPageLocators.first_name_field, first_name)
        self.send_text_to_element(OrderPageLocators.last_name_field, last_name)
        self.send_text_to_element(OrderPageLocators.address_field, address)
        self.send_text_to_element(OrderPageLocators.metro_field, metro)
        self.click_on_metro_option(metro)
        self.send_text_to_element(OrderPageLocators.phone_field, phone)
        self.scroll_to_element(OrderPageLocators.next_button)
        self.click_on_element(OrderPageLocators.next_button)
        self.wait_for_visibility(OrderPageLocators.date_field)

    @allure.step("Выбрать станцию метро {station_name}")
    def click_on_metro_option(self, station_name):
        locator = (OrderPageLocators.metro_option[0], OrderPageLocators.metro_option[1].format(station_name))
        self.click_on_element(locator)

    @allure.step("Заполнить вторую часть формы: дата {date}, срок {rental_period}, цвет {color}")
    def fill_second_form(self, date, rental_period, color, comment):
        self.send_text_to_element(OrderPageLocators.date_field, date)
        self.wait_for_attribute_contains(OrderPageLocators.date_field, "value", date)
        self.find_element_with_wait(OrderPageLocators.date_field).send_keys(Keys.ENTER)
        self.click_on_element(OrderPageLocators.dropdown)
        self.select_rental_period(rental_period)
        self.select_color(color)
        if comment:
            self.send_text_to_element(OrderPageLocators.comment_field, comment)

    @allure.step("Выбрать срок аренды {period}")
    def select_rental_period(self, period):
        locator = (OrderPageLocators.rental_period[0], OrderPageLocators.rental_period[1].format(period))
        self.click_on_element(locator)

    @allure.step("Выбрать цвет {color}")
    def select_color(self, color):
        locator = (OrderPageLocators.color_option[0], OrderPageLocators.color_option[1].format(color))
        self.click_on_element(locator)

    @allure.step("Отправить заказ")
    def submit_order(self):
        self.click_on_element(OrderPageLocators.submit_button)

    @allure.step("Подтвердить заказ в модальном окне")
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.confirm_button)

    @allure.step("Получить текст сообщения об успешном заказе")
    def get_success_message_text(self):
        return self.get_text_from_element(OrderPageLocators.success_message)
