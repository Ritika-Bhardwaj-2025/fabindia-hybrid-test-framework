from locators.fantastic_last_product_locators import FantasticLastProductLocators
from utilities.excelReader import ExcelReader
from time import sleep

class FantasticLastProductAction:
    def __init__(self,driver,helper,logger,screenshot):
        self.driver = driver
        self.helper = helper
        self.logger = logger
        self.screenshot = screenshot
        self.excel = ExcelReader("testdata/data.xlsx")

    def perform_action(self):
        try:
            self.logger.info("Verifying fantastic find fourth product")
            self.scroll_fantastic_finds()
            self.click_right_arrow()
            self.click_fourth_product()
            self.verify_product_page()
            self.logger.info("Successfully verified fantastic find fourth product")
        except Exception as e:
            self.logger.error(f"Failed to verify fantastic find fourth product: {str(e)}")

    def scroll_fantastic_finds(self):
        """
        method name: scroll_fantastic_finds
        Author name: Ritika Bhardwaj
        description: Scrolls to the Fantastic Finds section and verifies heading.
        parameter: None
        Return type: None
        """
        try:
            self.helper.scroll_to_pixels(0,2600)
            sleep(2)
            self.helper.scroll_to_pixels(0, 2650)
            sleep(2)
            self.helper.verify_in(FantasticLastProductLocators.FANTASTIC_FINDS_HEADING,str(self.excel.read_testcase_data(2,"testcase4")))
            self.logger.debug("Scrolled till fantastic finds")
        except Exception as e:
            self.logger.error(f"Failed to scroll till fantastic finds: {str(e)}")
            self.screenshot.capture_element_screenshot(self.helper.get_element(
                FantasticLastProductLocators.FANTASTIC_FINDS_HEADING),"error_scroll_finds")
            raise Exception(str(e))

    def click_right_arrow(self):
        """
        method name: click_right_arrow
        Author name: Ritika Bhardwaj
        description: Clicks the right arrow in the Fantastic Finds carousel.
        parameter: None
        Return type: None
        """
        try:
            self.helper.click_element(FantasticLastProductLocators.RIGHT_ARROW)
            self.screenshot.capture_element_screenshot(self.helper.get_element(
                FantasticLastProductLocators.RIGHT_ARROW),"verify_right_arrow")
            self.logger.debug("Clicked on right arrow")
        except Exception as e:
            self.logger.error(f"Failed to click right arrow: {str(e)}")
            self.screenshot.capture_element_screenshot(self.helper.get_element(
                FantasticLastProductLocators.RIGHT_ARROW), "error_right_arrow")
            raise Exception(str(e))

    def click_fourth_product(self):
        """
        method name: click_fourth_product
        Author name: Ritika Bhardwaj
        description: Clicks the fourth product in the Fantastic Finds section.
        parameter: None
        Return type: None
        """
        try:
            sleep(1)
            self.helper.click_element(FantasticLastProductLocators.FOURTH_PRODUCT)
            sleep(2)
            self.logger.debug("Clicked fourth product")
        except Exception as e:
            self.logger.error(f"Failed to click fourth product: {e}")
            self.screenshot.capture_screenshot(self.driver, "error_fourth_product")
            raise Exception(str(e))

    def verify_product_page(self):
        """
        method name: verify_product_page
        Author name: Ritika Bhardwaj
        description: Verifies that the product page is opened.
        parameter: None
        Return type: None
        """
        try:
            self.helper.verify_in(FantasticLastProductLocators.PRODUCT_PAGE_HEADING,str(self.excel.read_testcase_data(3,"testcase4")))
            self.logger.debug("Validated product page opened")
        except Exception as e:
            self.logger.error(f"Failed to open product page: {e}")
            self.screenshot.capture_element_screenshot(self.helper.get_element(
                FantasticLastProductLocators.PRODUCT_PAGE_HEADING),"error_open_page")
            raise Exception(str(e))
