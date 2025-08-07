import os
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class ScreenShot:
    def __init__(self, save_dir: str = "screenshot"):
        self.save_dir = save_dir
        os.makedirs(self.save_dir, exist_ok=True)

    def capture_screenshot(self, driver: WebDriver, method_name: str) -> str:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{method_name}_{timestamp}.png"
        filepath = os.path.join(self.save_dir, filename)

        driver.save_screenshot(filepath)
        return filepath

    def capture_element_screenshot(self, element: WebElement, method_name: str) -> str:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{method_name}_{timestamp}.png"
        filepath = os.path.join(self.save_dir, filename)

        element.screenshot(filepath)
        return filepath
