from selenium.webdriver.common.by import By


class OrderPageLocators:
    first_name_field = (By.XPATH, ".//input[contains(@placeholder, 'Имя')]")
    last_name_field = (By.XPATH, ".//input[contains(@placeholder, 'Фамилия')]")
    address_field = (By.XPATH, ".//input[contains(@placeholder, 'Адрес')]")
    metro_field = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    phone_field = (By.XPATH, ".//input[contains(@placeholder, 'Телефон')]")
    next_button = (By.XPATH, ".//button[text()='Далее']")
    date_field = (By.XPATH, ".//*[contains(@placeholder, 'Когда')]")
    dropdown = (By.XPATH, ".//div[contains(@class, 'Dropdown-root')]")
    comment_field = (By.XPATH, ".//input[contains(@placeholder, 'Комментарий')]")
    confirm_button = (By.XPATH, ".//button[text()='Да']")
    success_message = (By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]")
    metro_option = (By.XPATH, "//div[text()='{}']")
    rental_period = (By.XPATH, "//div[text()='{}']")
    color_option = (By.XPATH, ".//label[contains(text(), '{}')]")
    submit_button = (By.XPATH, "(//button[text()='Заказать'])[last()]")
