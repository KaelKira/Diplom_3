from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:

    RESER_PASSWORD_LINK = (By.XPATH, './/a[text()="Восстановить пароль"]')
    RESER_PASSWORD_BUTTON = (By.XPATH, './/button[text()="Восстановить"]')
    EMAIL_FOR_RESTORE = (By.XPATH, './/input')
    NEW_PASSWORD_INPUT = (By.XPATH, './/input[@name = "Введите новый пароль"]')
    EYE = (By.XPATH, './/div[@class = "input__icon input__icon-action"]')
    FOCUSED_INPUT_BORDER = (By.XPATH, './/div[@class = "input__container"]/div')
