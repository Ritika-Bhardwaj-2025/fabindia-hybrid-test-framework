from selenium.common import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

class WebDriverHelper:
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            return element
        except WebDriverException as e:
            print(e)
            raise Exception (str(e))

    def click_element(self,locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            element.click()
        except WebDriverException as e:
            print(e)
            raise Exception (str(e))

    def hover_one_element(self,locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            ActionChains(self.driver).move_to_element(element).perform()
        except WebDriverException as e:
            print(e)
            raise Exception (str(e))

    def fill_form(self,locator,text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except WebDriverException as e:
            print(e)
            raise Exception (str(e))

    def fill_form_enter(self,locator,text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            element.send_keys(Keys.ENTER)
        except WebDriverException as e:
            print(e)
            raise Exception (str(e))

    def switch_window(self):
        try:
            windows = self.driver.window_handles[1]
            self.driver.switch_to.window(windows)
        except WebDriverException as e:
            print(e)
            raise Exception (str(e))

    def js_scroll(self,locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView();",element)
        except WebDriverException as e:
            print(e)
            raise Exception (str(e))

    def verify_in(self,locator,text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            element_text = element.text
            assert text in element_text
        except WebDriverException as e:
            print(e)
            raise Exception (str(e))

    def verify_text(self,expected_text,text):
        try:
            assert text in expected_text
        except WebDriverException as e:
            print(e)
            raise Exception (str(e))

    def scroll_by_pixels(self, x, y):
        try:
            self.driver.execute_script(f"window.scrollBy({x}, {y});")
        except Exception as e:
            print(e)
            raise Exception(str(e))

    def scroll_to_pixels(self, x, y):
        try:
            self.driver.execute_script(f"window.scrollTo({x}, {y});")
        except Exception as e:
            print(e)
            raise Exception(str(e))

    def scroll_by_keys(self, locator, num):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            for i in range(num):
                element.send_keys(Keys.DOWN)
        except Exception as e:
            print(e)
            raise Exception(str(e))

    def js_click_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            self.driver.execute_script("arguments[0].click();", element)
        except WebDriverException as e:
            print(e)
            raise Exception(str(e))

