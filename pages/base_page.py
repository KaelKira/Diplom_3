from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = Constants.MAIN_URL

    def go_to_site(self):
        self.driver.get(self.url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator), message = f'Not find element{locator}')

    def find_element_and_click(self, locator, time=10):
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator), message = f'Not find element{locator}').click()

    def find_element_get_text(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator), message = f'Not find element{locator}').text

    def send_key(self, locator, key, time=10):
        WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                               message=f'Not find element{locator}').send_keys(key)

    def find_element_get_class(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                                      message=f'Not find element{locator}').get_attribute("class")
    def find_element_get_type(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                                      message=f'Not find element{locator}').get_attribute("type")
    def find_element_get_value(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                                      message=f'Not find element{locator}').get_attribute("value")

    def drag_and_drop_on_element(self, locator_one, locator_two, time=10):
        draggable = WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator_one), message = f'Not find element{locator_one}')
        droppable = WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator_two), message = f'Not find element{locator_two}')
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()

    def switch_window(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[1])

    def get_url(self):
        return self.driver.current_url

    def waiting_element_strong_visible(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.staleness_of(self.driver.find_element(locator)))

        new_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator)  # Найти новый элемент
        )

        return new_element.text