from constants import Constants
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage
import allure


class ResetPasswordPage(BasePage):

    @allure.step('click_on_reset_password_link')
    def click_on_reset_password_link(self):
        self.find_element_and_click(ResetPasswordPageLocators.RESER_PASSWORD_LINK)

    @allure.step('enter_email_to_restore')
    def enter_email_to_restore(self):
        self.send_key(ResetPasswordPageLocators.EMAIL_FOR_RESTORE, Constants.EMAIL)

    @allure.step('click_on_reset_password_button')
    def click_on_reset_password_button(self):
        self.find_element_and_click(ResetPasswordPageLocators.RESER_PASSWORD_BUTTON)

    @allure.step('enter_email_to_restore')
    def enter_new_password(self):
        self.send_key(ResetPasswordPageLocators.NEW_PASSWORD_INPUT, Constants.NEW_PASSWORD)

    @allure.step('click_on_eye')
    def click_on_eye(self):
        self.find_element_and_click(ResetPasswordPageLocators.EYE)

    @allure.step('check_focused_border')
    def check_focused_border(self):
        class_to_check = self.find_element_get_class(ResetPasswordPageLocators.FOCUSED_INPUT_BORDER)
        assert 'input_status_active' in class_to_check

    @allure.step('check_focused_text')
    def check_focused_text(self):
        type_to_check = self.find_element_get_type(ResetPasswordPageLocators.NEW_PASSWORD_INPUT)
        assert 'text' in type_to_check