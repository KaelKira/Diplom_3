from selenium.webdriver.common.by import By

class OrdersPageLocators:
    ORDERS_LIST_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]') # Заголовок "Лента заказов"
    ORDER_STRUCTURE = By.XPATH, '//p[text()="Cостав"]'  # Состав
    ORDER_LINK = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'  # ссылка на заказ в Ленте заказов
    ALL_ORDERS_AT_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, "
                                       "'text_type_digits-default')]")
    ALL_ORDERS_AT_FEED = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                                    "text_type_digits-default']")

    TOTAL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DAILY_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    NUMBER_IN_PROGRESS_2 = (By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li')  # Номер в разделе "В работе"
    NUMBER_IN_PROGRESS = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem "
                                         "OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")

    FIRST_ORDER = (By.XPATH, './/div[@class = "OrderFeed_contentBox__3-tWb"]/ul/li')
    ORDER_DETAIL = (By.XPATH, '//p[text()="Cостав"]')
    ORDERS_COUNT = (By.XPATH, './/div[@class = "undefined mb-15"]/p[2]')
    ORDERS_COUNT_TODAY = (By.XPATH, './/p[text() = "Выполнено за сегодня:"]/parent::div/p[2]')
    ORDERS_COUNT_IN_PROGRES = (By.XPATH, './/p[text() = "В работе:"]/parent::div/ul[2]/li')