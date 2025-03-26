import allure
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage


class TestResetPassword:

    @allure.title('Восстановление пароля')
    def test_order_form_header(self, driver):
        main_page = MainPage(driver)
        reset_password = ResetPasswordPage(driver)
        main_page.click_on_enter_to_profile_button()
        reset_password.click_on_reset_password_link()
        reset_password.enter_email_to_restore()
        reset_password.click_on_reset_password_button()
        reset_password.enter_new_password()
        reset_password.click_on_eye()
        reset_password.check_focused_border()
        reset_password.check_focused_text()