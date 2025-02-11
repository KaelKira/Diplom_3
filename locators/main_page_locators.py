from selenium.webdriver.common.by import By
from constants import Constants


class MainPageLocators:
    EMAIL = (By.XPATH, './/label[text()="Email"]/parent::div/input')
    PASSWORD = (By.XPATH, './/label[text()="Пароль"]/parent::div/input')
    AUTH_BUTTON = (By.XPATH, './/button[text() = "Войти"]')
    ORDER_LIST_HEADER = (By.XPATH, './/h1[text()="Лента заказов"]')
    ORDER_LIST = (By.XPATH, './/p[text() = "Лента Заказов"]')

    CONSTRACTOR_TAB = (By.XPATH, './/p[text()="Конструктор"]')
    CONSTRACTOR_HEADER = (By.XPATH, './/h1')
    COUNTER = (By.XPATH, './/p[@class = "counter_counter__num__3nue1"]')
    ORDER_BASKET = (By.XPATH, '//span[text()="Перетяните булочку сюда (низ)"]')

    MAKE_AN_ORDER = (By.XPATH, './/button[text()="Оформить заказ"]')
    SUCCESS = (By.XPATH, './/p[text() = "Ваш заказ начали готовить"]')
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    CLOSE_MODAL_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]")


    BUN = (By.XPATH, './/p[text()="Флюоресцентная булка R2-D3"]')
    CLOSE_MARKER = (By.XPATH, './/button[@class = "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    BUN_DETAIL = (By.XPATH, './/h2[text()="Детали ингредиента"]')
    MODAL = (By.XPATH, './/section[@class = "Modal_modal__P3_V5"]')


    PROFILE = (By.XPATH, './/p[text()="Личный Кабинет"]')
    HEADER = (By.XPATH, './/h1[text()="Соберите бургер"]')
    ENTER_TO_PROFILE_BUTTON = (By.XPATH, './/button[text() = "Войти в аккаунт"]')
    LOGO = (By.XPATH, './/header/nav/div')

    ENTER_LINK = (By.XPATH, './/a[text()="Войти"]')
    FOR_EMAIL = (By.XPATH, f'.//input[@value = "{Constants.EMAIL}"]')