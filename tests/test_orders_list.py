import time

import allure
from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from pages.orders_list_page import OrderListPage
from pages.profile_page import ProfilePage


class TestOrderListPage:

    @allure.title('Проверка если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_popup_detail(self, driver):
        main_page = MainPage(driver)
        orders_list = OrderListPage(driver)
        main_page.click_orders_list()
        orders_list.first_order_click()
        orders_list.check_order_detail()


    @allure.title('Заказ пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,')
    def test_order_list_id_compare(self, driver):
        main_page = MainPage(driver)
        orders_list = OrderListPage(driver)
        order_id = main_page.make_order_and_get_id()
        main_page.click_close_modal_order()
        main_page.click_orders_list()
        locator = (By.XPATH, f'.//p[text() = {order_id}]')
        text = orders_list.find_order_by_id(locator)
        assert text == order_id

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_order_list_counter_increased(self, driver):
        main_page = MainPage(driver)
        orders_list = OrderListPage(driver)
        main_page.click_orders_list()
        old_count = int(orders_list.get_total_orders_number()) + 1
        main_page.click_constractor()
        main_page.make_order_and_get_id()
        main_page.click_close_modal_order()
        main_page.click_orders_list()
        new_count = int(orders_list.get_total_orders_number())
        assert old_count == new_count

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_order_list_id_compare(self, driver):
        main_page = MainPage(driver)
        orders_list = OrderListPage(driver)
        main_page.click_orders_list()
        old_count = int(orders_list.get_total_orders_number_today()) + 1
        main_page.click_constractor()
        main_page.make_order_and_get_id()
        main_page.click_close_modal_order()
        main_page.click_orders_list()
        new_count = int(orders_list.get_total_orders_number_today())
        assert old_count == new_count

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_order_list_id_compare(self, driver):
        main_page = MainPage(driver)
        orders_list = OrderListPage(driver)
        order_id = main_page.make_order_and_get_id()
        main_page.click_close_modal_order()
        main_page.click_orders_list()
        time.sleep(3)
        orders_list_in_progress = orders_list.get_orders_in_progress()
        assert order_id in orders_list_in_progress