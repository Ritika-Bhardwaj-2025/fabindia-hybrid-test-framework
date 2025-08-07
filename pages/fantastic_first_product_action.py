from locators.fantastic_first_product_locators import FantasticFirstProductLocators
from utilities.excelReader import ExcelReader
from time import sleep

class FantasticFirstProductAction:
    def __init__(self,driver,helper,logger,screenshot):
        self.driver = driver
        self.helper = helper
        self.logger = logger
        self.screenshot = screenshot
        self.excel = ExcelReader("testdata/data.xlsx")

    def perform_action(self):
        try:
            self.logger.info("Verifying fantastic find first banner")
            self.scroll_fantastic_finds()
            self.click_first_product()
            self.verify_product_page()
            self.hover_click_third_product()
            self.verify_select_size_action()
            self.logger.info("Successfully verified fantastic find first banner")
        except Exception as e:
            self.logger.error(f"Failed to verify fantastic find first banner: {str(e)}")

    def scroll_fantastic_finds(self):
        """
        method name: scroll_fantastic_finds
        Author name: Ritika Bhardwaj
        description: Scrolls to the Fantastic Finds section and verifies heading.
        parameter: None
        Return type: None
        """
        try:
            self.helper.scroll_to_pixels(0, 2600)
            sleep(2)
            self.helper.scroll_to_pixels(0, 2650)
            sleep(2)
            self.helper.verify_in(FantasticFirstProductLocators.FANTASTIC_FINDS_HEADING,str(self.excel.read_testcase_data(2,"testcase3")))
            self.logger.debug("Scrolled till fantastic finds section")
        except Exception as e:
            self.logger.error(f"Failed to scroll till fantastic finds: {str(e)}")
            self.screenshot.capture_element_screenshot(self.helper.get_element(
                FantasticFirstProductLocators.FANTASTIC_FINDS_HEADING),"error_scroll_finds")
            raise Exception(str(e))

    def click_first_product(self):
        """
        method name: click_first_product
        Author name: Ritika Bhardwaj
        description: Clicks the first product in the Fantastic Finds section.
        parameter: None
        Return type: None
        """
        try:
            sleep(3)
            self.helper.click_element(FantasticFirstProductLocators.FIRST_PRODUCT)
            sleep(2)
            self.logger.debug("Clicked on first product")
        except Exception as e:
            self.logger.error(f"Failed to click first product: {str(e)}")
            self.screenshot.capture_screenshot(self.driver, "error_first_product")
            raise Exception (str(e))

    def verify_product_page(self):
        """
        method name: verify_product_page
        Author name: Ritika Bhardwaj
        description: Verifies that the product page is opened.
        parameter: None
        Return type: None
        """
        try:
            self.helper.verify_in(FantasticFirstProductLocators.PRODUCT_PAGE_HEADING,str(self.excel.read_testcase_data(3,"testcase3")))
            self.logger.debug("Verified product page opened")
        except Exception as e:
            self.logger.error(f"Failed to open product page: {str(e)}")
            self.screenshot.capture_element_screenshot(self.helper.get_element(
                FantasticFirstProductLocators.PRODUCT_PAGE_HEADING),"error_open_page")
            raise Exception(str(e))

    def hover_click_third_product(self):
        """
        Method: hover_click_third_product
        Author: Ritika Bhardwaj
        Description: Hovers over the third product and clicks it.
        Parameters: None
        Returns: None
        """
        sleep(2)
        try:
            self.helper.js_scroll(FantasticFirstProductLocators.THIRD_PRODUCT_DIV)
            self.driver.implicitly_wait(5)
            self.helper.hover_one_element(FantasticFirstProductLocators.THIRD_PRODUCT_DIV)
            self.driver.implicitly_wait(5)
            self.helper.click_element(FantasticFirstProductLocators.THIRD_PRODUCT)
            self.logger.debug("Clicked on third product from product list")
        except Exception as e:
            self.logger.error(f"Failed to click third product: {str(e)}")
            self.screenshot.capture_screenshot(self.driver, "error_third_product")
            raise Exception(str(e))

    def verify_select_size_action(self):
        """
        Method: verify_select_size_action
        Author: Ritika Bhardwaj
        Description: Verifies that the product page is opened by checking for 'select size' text.
        Parameters: None
        Returns: None
        """
        try:
            self.helper.switch_window()
            self.helper.verify_in(FantasticFirstProductLocators.SELECT_SIZE_TEXT, str(self.excel.read_testcase_data(4,"testcase3")))
            self.logger.debug("Validated product page opened")
        except Exception as e:
            self.logger.error(f"Failed to open product page: {str(e)}")
            self.screenshot.capture_screenshot(self.driver, "error_first_product")
            raise Exception(str(e))
