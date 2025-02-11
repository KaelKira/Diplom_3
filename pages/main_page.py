from constants import Constants
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    @allure.step('click_on_yandex_logo')
    def click_on_enter_to_profile_button(self):
        self.find_element_and_click(MainPageLocators.ENTER_TO_PROFILE_BUTTON)

    @allure.step('click_on_profile')
    def click_on_profile(self):
        self.find_element_and_click(MainPageLocators.PROFILE)

    @allure.step('fill_the_login_form')
    def fill_the_login_form(self):
        self.send_key(MainPageLocators.EMAIL, Constants.EMAIL)
        self.send_key(MainPageLocators.PASSWORD, Constants.PASSWORD)

    @allure.step('click_on_login_button')
    def click_on_login_button(self):
        self.find_element_and_click(MainPageLocators.AUTH_BUTTON)

    @allure.step('login_into_profile')
    def login_into_profile(self):
        self.click_on_enter_to_profile_button()
        self.fill_the_login_form()
        self.click_on_login_button()

    @allure.step('click_orders_list')
    def click_orders_list(self):
        self.find_element_and_click(MainPageLocators.ORDER_LIST)

    @allure.step('check_orders_list')
    def check_orders_list(self):
        text = self.find_element_get_text(MainPageLocators.ORDER_LIST_HEADER)
        assert 'Лента заказов' == text

    @allure.step('click_constractor')
    def click_constractor(self):
        self.find_element_and_click(MainPageLocators.CONSTRACTOR_TAB)

    @allure.step('login_into_profile')
    def check_constractor(self):
        text = self.find_element_get_text(MainPageLocators.CONSTRACTOR_HEADER)
        assert 'Соберите бургер' == text

    @allure.step('click_ingredient')
    def click_ingredient(self):
        self.find_element_and_click(MainPageLocators.BUN)

    @allure.step('check_detail_ingredient')
    def check_detail_ingredient(self):
        text = self.find_element_get_text(MainPageLocators.BUN_DETAIL)
        assert 'Детали ингредиента' == text

    @allure.step('click_close_details')
    def click_close_details(self):
        self.find_element_and_click(MainPageLocators.CLOSE_MARKER)

    @allure.step('check_close_details')
    def check_close_details(self):
        class_to_check = self.find_element_get_class(MainPageLocators.MODAL)
        assert 'Modal_modal_opened__3ISw4' not in class_to_check

    @allure.step('add_filling_to_order')
    def add_filling_to_order(self):
        self.drag_and_drop_on_element(MainPageLocators.BUN, MainPageLocators.ORDER_BASKET)

    @allure.step('click_on_order_button')
    def click_on_order_button(self):
        self.find_element_and_click(MainPageLocators.MAKE_AN_ORDER)

    @allure.step('get_count_value')
    def check_count_value_zero(self):
        text = self.find_element_get_text(MainPageLocators.COUNTER)
        assert text == '0'

    @allure.step('get_count_value')
    def check_count_value_increased(self):
        text = self.find_element_get_text(MainPageLocators.COUNTER)
        assert text == '2'

    @allure.step('Получение ORDER_ID')
    def get_with_order_id(self):
        order_id = self.find_element_get_text(MainPageLocators.ORDER_ID)
        while order_id == '9999':
            order_id = self.find_element_get_text(MainPageLocators.ORDER_ID)
        return f"{order_id}"

    @allure.step("click_close_modal_order")
    def click_close_modal_order(self):
        self.find_element_and_click(MainPageLocators.CLOSE_MODAL_ORDER)

    @allure.title('make_order_and_get_id')
    def make_order_and_get_id(self):
        self.login_into_profile()
        self.add_filling_to_order()
        self.click_on_order_button()
        self.get_with_order_id()
        order_id = self.get_with_order_id()
        return f"{order_id}"
