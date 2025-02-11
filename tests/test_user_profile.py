import time
import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestUserProfile:

    @allure.title('Вход в аккаунт и переход в него по кнопке Личный Кабинет')
    def test_enter_to_profile(self, driver):
        main_page = MainPage(driver)
        profile = ProfilePage(driver)
        main_page.login_into_profile()
        main_page.click_on_profile()
        profile.check_email_into_profile()

    @allure.title('Профиль - переход на историю заказов')
    def test_history(self, driver):
        main_page = MainPage(driver)
        profile = ProfilePage(driver)
        main_page.login_into_profile()
        main_page.click_on_profile()
        profile.click_on_history_list()
        profile.check_history()

    @allure.title('Профиль - переход на историю заказов')
    def test_history(self, driver):
        main_page = MainPage(driver)
        profile = ProfilePage(driver)
        main_page.login_into_profile()
        main_page.click_on_profile()
        profile.logout()
        profile.check_logout()
