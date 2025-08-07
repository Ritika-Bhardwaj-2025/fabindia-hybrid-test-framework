from locators.festive_locators import FestiveLocators
from utilities.excelReader import ExcelReader
from time import sleep

class FestiveAction:
    def __init__(self, driver, helper, logger, screenshot):
        self.driver = driver
        self.helper = helper
        self.logger = logger
        self.screenshot = screenshot
        self.excel = ExcelReader("testdata/data.xlsx")

    def perform_action(self):
        try:
            self.logger.info("Verifying festive collection url function")
            sleep(2)
            self.click_right_arrow()
            sleep(2)
            self.click_right_arrow()
            sleep(2)
            self.click_third_banner()
            self.verify_product_page()
            self.verify_url_page_action()
            self.logger.info("Successfully verified festive collection url function")
        except Exception as e:
            self.logger.error(f"Failed to verify festive collection url function: {str(e)}")

    def click_right_arrow(self):
        """
        Method Name: click_right_arrow
        Author: Ritika Bhardwaj
        Description: Clicks the right arrow in the festive carousel.
        Parameters: None
        Return Type: None
        """
        try:
            self.helper.click_element(FestiveLocators.ARROW_RIGHT)
            self.screenshot.capture_element_screenshot(self.helper.get_element(
                FestiveLocators.ARROW_RIGHT),"verify_right_arrow")
            self.logger.debug("Clicked right arrow")
        except Exception as e:
            self.logger.error(f"Failed to click right arrow: {e}")
            self.screenshot.capture_element_screenshot(self.helper.get_element(
                FestiveLocators.ARROW_RIGHT), "error_right_arrow")
            raise Exception (str(e))

    def click_third_banner(self):
        """
        Method Name: click_third_banner
        Author: Ritika Bhardwaj
        Description: Clicks the third banner in the festive carousel.
        Parameters: None
        Return Type: None
        """
        try:
            self.helper.click_element(FestiveLocators.BANNER_CAROUSEL_THIRD)
            self.screenshot.capture_screenshot(self.driver, "verify_banner_loaded")
            self.logger.debug("Banner is fully loaded")
        except Exception as e:
            self.logger.error(f"Failed to load the banner: {e}")
            self.screenshot.capture_screenshot(self.driver, "error_banner_loaded")
            raise Exception(str(e))

    def verify_product_page(self):
        """
        Method Name: verify_product_page
        Author: Ritika Bhardwaj
        Description: Verifies the product listing page is opened.
        Parameters: None
        Return Type: None
        """
        try:
            self.helper.verify_in(FestiveLocators.PRODUCT_PAGE_TITLE, str(self.excel.read_testcase_data(2,"testcase8")))
            self.logger.debug("Validated the product listing page is opened")
            self.screenshot.capture_element_screenshot(
                self.helper.get_element(FestiveLocators.PRODUCT_PAGE_TITLE),
                "error_product_page"
            )
        except Exception as e:
            self.logger.error(f"Failed to open product listing page: {e}")
            self.screenshot.capture_element_screenshot(
                self.helper.get_element(FestiveLocators.PRODUCT_PAGE_TITLE),
                "error_product_page"
            )
            raise Exception(str(e))

    def verify_url_page_action(self):
        """
        Method Name: verify_url_page_action
        Author: Ritika Bhardwaj
        Description: Verifies the current page URL.
        Parameters: None
        Return Type: None
        """
        try:
            url = self.driver.current_url
            self.helper.verify_text(FestiveLocators.CURRENT_PAGE_URL,url)
            self.logger.debug("validated url is correct")
        except Exception as e:
            self.logger.warning(f"Failed to verify url: {e}")
            self.screenshot.capture_screenshot(self.driver,"error_url")
            raise Exception(str(e))
