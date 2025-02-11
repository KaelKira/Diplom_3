from locators.order_list_page_locators import OrdersPageLocators
from pages.base_page import BasePage
import allure


class OrderListPage(BasePage):

    @allure.step('first_order_click')
    def first_order_click(self):
        self.find_element_and_click(OrdersPageLocators.FIRST_ORDER)

    @allure.step('first_order_click')
    def check_order_detail(self):
        text = self.find_element_get_text(OrdersPageLocators.ORDER_DETAIL)
        assert text == 'Cостав'

    @allure.step('first_order_click')
    def find_order_by_id(self, locator):
        text = self.find_element_get_text(locator)
        return text

    @allure.step('first_order_click')
    def get_total_orders_number(self):
        orders_count = self.find_element_get_text(OrdersPageLocators.ORDERS_COUNT)
        return f'{orders_count}'

    @allure.step('first_order_click')
    def get_total_orders_number_today(self):
        orders_count = self.find_element_get_text(OrdersPageLocators.ORDERS_COUNT_TODAY)
        return f'{orders_count}'

    @allure.step('first_order_click')
    def get_orders_in_progress(self):
        orders_id = self.find_element_get_text(OrdersPageLocators.ORDERS_COUNT_IN_PROGRES)
        return f'{orders_id}'