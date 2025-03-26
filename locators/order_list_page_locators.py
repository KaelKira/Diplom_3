from selenium.webdriver.common.by import By

class OrdersPageLocators:
    FIRST_ORDER = (By.XPATH, './/div[@class = "OrderFeed_contentBox__3-tWb"]/ul/li')
    ORDER_DETAIL = (By.XPATH, '//p[text()="Cостав"]')
    ORDERS_COUNT = (By.XPATH, './/div[@class = "undefined mb-15"]/p[2]')
    ORDERS_COUNT_TODAY = (By.XPATH, './/p[text() = "Выполнено за сегодня:"]/parent::div/p[2]')
    ORDERS_COUNT_IN_PROGRES = (By.XPATH, './/p[text() = "В работе:"]/parent::div/ul[2]/li')