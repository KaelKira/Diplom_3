from constants import Constants
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage
import allure


class ProfilePage(BasePage):
    @allure.step('click_on_history_list')
    def click_on_history_list(self):
        self.find_element_and_click(ProfilePageLocators.HISTORY)

    @allure.step('check_email_into_profile')
    def check_email_into_profile(self):
        element = self.find_element_get_value(ProfilePageLocators.EMAIL_IN_PROFILE)
        assert Constants.EMAIL == element

    @allure.step('check_history')
    def check_history(self):
        element = self.find_element_get_text(ProfilePageLocators.DONE_TEXT)
        assert 'Выполнен' == element

    @allure.step('logout')
    def logout(self):
        self.find_element_and_click(ProfilePageLocators.EXIT)

    @allure.step('check_logout')
    def check_logout(self):
        element = self.find_element_get_text(ProfilePageLocators.LOGOUT_ENTER)
        assert 'Вход' == element

    @allure.step('Получение ORDER_ID')
    def get_order_id(self):
        order_id = self.find_element_get_text(ProfilePageLocators.PROFILE_ORDER_ID)
        return f"{order_id}"