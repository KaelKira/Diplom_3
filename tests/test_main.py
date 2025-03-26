import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestMainPage:

    @allure.title('Переход на таб Лента заказов')
    def test_order_list_move(self, driver):
        main_page = MainPage(driver)
        main_page.click_orders_list()
        main_page.check_orders_list()

    @allure.title('Переход на таб Конструктов')
    def test_constractor_move(self, driver):
        main_page = MainPage(driver)
        main_page.click_orders_list()
        main_page.check_orders_list()
        main_page.click_constractor()
        main_page.check_constractor()

    @allure.title('Открытие деталей ингредиента')
    def test_detail_presence(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.check_detail_ingredient()

    @allure.title('Закрытие деталей ингредиента')
    def test_detail_close(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.check_detail_ingredient()
        main_page.click_close_details()
        main_page.check_close_details()

    @allure.title('Увеличение счётчика у ингридиента')
    def test_count_increase(self, driver):
        main_page = MainPage(driver)
        main_page.check_count_value_zero()
        main_page.add_filling_to_order()
        main_page.check_count_value_increased()

    @allure.title('Создание заказа')
    def test_order_create(self, driver):
        main_page = MainPage(driver)
        profile = ProfilePage(driver)
        main_page.login_into_profile()
        main_page.add_filling_to_order()
        main_page.click_on_order_button()
        main_page.get_with_order_id()
        order_number = main_page.get_with_order_id()
        main_page.click_close_modal_order()
        main_page.click_on_profile()
        profile.click_on_history_list()
        profile_order_id = profile.get_order_id()
        assert order_number and profile_order_id