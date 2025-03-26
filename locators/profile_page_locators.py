from selenium.webdriver.common.by import By
from constants import Constants


class ProfilePageLocators:

    PROFILE = (By.XPATH, './/p[text()="Личный Кабинет"]')
    EMAIL_IN_PROFILE = (By.XPATH, f'.//input[@value = "{Constants.EMAIL}"]')
    HISTORY = (By.XPATH, './/a[text()="История заказов"]')
    DONE_TEXT = (By.XPATH, './/p[text()="Выполнен"]')
    EXIT = (By.XPATH, './/button[text()= "Выход"]')
    LOGOUT_ENTER = (By.XPATH, './/h2[text()="Вход"]')
    PROFILE_ORDER_ID = (By.XPATH, './/p[@class = "text text_type_digits-default"][1]')
