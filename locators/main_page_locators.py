from selenium.webdriver.common.by import By


class MainPageLocators:
    question = (By.ID, "accordion__heading-{}")
    answer = (By.ID, "accordion__panel-{}")
