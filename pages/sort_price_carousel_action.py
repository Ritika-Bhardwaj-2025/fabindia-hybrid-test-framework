from selenium.webdriver.support.select import Select
from locators.sort_price_carousel_locators import SortPriceCarouselLocators
from utilities.excelReader import ExcelReader
from time import sleep

class SortPriceCarouselAction:
    def __init__(self,driver,helper,logger,screenshot):
        self.driver = driver
        self.helper = helper
        self.logger = logger
        self.screenshot = screenshot
        self.excel = ExcelReader("testdata/data.xlsx")

    def perform_action(self):
        try:
            self.logger.info("Verifying carousel product filtering function")
            self.click_banner_carousel_action()
            self.verify_product_page_action()
            self.select_filter_price_action()
            self.verify_price_click_action()
            self.hover_click_second_product()
            self.verify_size_guide_action()
            self.scroll_till_similar_product()
            self.logger.info("Successfully verified carousel product filtering function")
        except Exception as e:
            self.logger.error(f"Failed to verify carousel product filtering function: {str(e)}")


    def click_banner_carousel_action(self):
        """
        Method: click_banner_carousel_action
        Author: Ritika Bhardwaj
        Description: Clicks on the first banner carousel element.
        Parameters: None
        Returns: None
        """
        try:
            self.helper.click_element(SortPriceCarouselLocators.BANNER_CAROUSEL_FIRST)
            self.logger.debug("Clicked on first carousel")
        except Exception as e:
            self.logger.error(f"Failed to click on first carousel: {e}")
            self.screenshot.capture_screenshot(self.driver, "error_first_carousel")
            raise Exception(str(e))

    def verify_product_page_action(self):
        """
        Method: verify_product_page_action
        Author: Ritika Bhardwaj
        Description: Verifies that the product listing page is opened.
        Parameters: None
        Returns: None
        """
        try:
            self.helper.verify_in(SortPriceCarouselLocators.FESTIVE_HEADING, str(self.excel.read_testcase_data(2,"testcase7")))
            self.logger.debug("Validated the product listing page is opened")
            self.screenshot.capture_element_screenshot(
                self.helper.get_element(SortPriceCarouselLocators.FESTIVE_HEADING),
                "error_festive_page"
            )
        except Exception as e:
            self.logger.error(f"Failed to open product listing page: {e}")
            self.screenshot.capture_element_screenshot(
                self.helper.get_element(SortPriceCarouselLocators.FESTIVE_HEADING),
                "error_festive_page"
            )
            raise Exception(str(e))

    def select_filter_price_action(self):
        """
        Method name: select_filter_price_action
        Author: Ritika Bhardwaj
        Description: Selects the 'Price: High to Low' option from the sort-by dropdown.
        Parameters: None
        Return Type: None
        """
        try:
            dropdown = Select(self.helper.get_element(SortPriceCarouselLocators.SORT_BY_DROPDOWN))
            dropdown.select_by_value(str(self.excel.read_testcase_data(3,"testcase7")))
            self.logger.debug("Selected price high to low from sort by dropdown")
        except Exception as e:
            self.logger.error("Failed to select price high to low from dropdown")
            self.screenshot.capture_element_screenshot(self.helper.get_element(),"error_price")
            raise Exception(str(e))

    def verify_price_click_action(self):
        """
        Method Name: verify_price_click_action
        Author: Ritika Bhardwaj
        Description: Verifies 'Price: High to Low' is selected.
        Parameters: None
        Return Type: None
        """
        try:
            self.helper.verify_in(SortPriceCarouselLocators.PRICE_HIGH_LOW_TEXT, str(self.excel.read_testcase_data(4,"testcase7")))
            self.logger.debug("Validated price high to low is been selected")
        except Exception as e:
            self.logger.error(f"Failed to select price from sort by dropdown: {e}")
            self.screenshot.capture_screenshot(self.driver, "error_price")
            raise Exception(str(e))

    def hover_click_second_product(self):
        """
        Method: hover_click_second_product
        Author: Ritika Bhardwaj
        Description: Hovers over the second product and clicks it.
        Parameters: None
        Returns: None
        """
        sleep(2)
        try:
            self.helper.js_scroll(SortPriceCarouselLocators.SECOND_PRODUCT_DIV)
            self.driver.implicitly_wait(5)
            self.helper.hover_one_element(SortPriceCarouselLocators.SECOND_PRODUCT_DIV)
            self.driver.implicitly_wait(5)
            self.helper.click_element(SortPriceCarouselLocators.SECOND_PRODUCT)
            self.logger.debug("Clicked on second product")
        except Exception as e:
            self.logger.error(f"Failed to click second product: {e}")
            self.screenshot.capture_screenshot(self.driver, "error_second_product")
            raise Exception(str(e))

    def verify_size_guide_action(self):
        """
        Method: verify_size_guide_action
        Author: Ritika Bhardwaj
        Description: Verifies that the product page is opened by checking for 'Size Guide' text.
        Parameters: None
        Returns: None
        """
        try:
            self.helper.switch_window()
            self.helper.verify_in(SortPriceCarouselLocators.SELECT_SIZE_TEXT, str(self.excel.read_testcase_data(5,"testcase7")))
            self.logger.debug("Validated product page opened")
        except Exception as e:
            self.logger.error(f"Failed to open product page: {e}")
            self.screenshot.capture_screenshot(self.driver, "error_first_product")
            raise Exception(str(e))

    def scroll_till_similar_product(self):
        """
        Method Name: scroll_till_similar_product
        Author: Ritika Bhardwaj
        Description: Scrolls to 'Similar Product' section.
        Parameters: None
        Return Type: None
        """
        try:
            sleep(3)
            self.helper.scroll_to_pixels(0,1500)
            sleep(2)
            self.helper.verify_in(SortPriceCarouselLocators.SIMILAR_PRODUCT_HEADING,str(self.excel.read_testcase_data(6,"testcase7")))
            self.logger.debug("Scrolled till similar product")
        except Exception as e:
            self.logger.error(f"Failed to scroll till similar product: {e}")
            self.screenshot.capture_screenshot(self.driver,"error_similar_product_heading")
            raise Exception (str(e))

