from selenium.webdriver.support.select import Select
from locators.sort_filter_carousel_locators import SortValidCarouselLocators
from utilities.excelReader import ExcelReader
from time import sleep

class SortValidCarousel:
    def __init__(self,driver,helper,logger,screenshot):
        self.driver = driver
        self.helper = helper
        self.logger = logger
        self.screenshot = screenshot
        self.excel = ExcelReader("testdata/data.xlsx")

    def perform_action(self):
        try:
            self.logger.info("Verifying similar product with filter")
            self.click_banner_carousel_action()
            self.verify_product_page_action()
            self.select_filter_bestseller_action()
            self.verify_bestseller_click_action()
            self.hover_click_second_product()
            self.verify_size_guide_action()
            self.scroll_till_similar_product()
            self.click_first_similar_product()
            self.verify_similar_product_page()
            self.logger.info("Successfully verified similar product with filter")
        except Exception as e:
            self.logger.error(f"Failed to verify similar product with filter: {str(e)}")


    def click_banner_carousel_action(self):
        """
        Method: click_banner_carousel_action
        Author: Ritika Bhardwaj
        Description: Clicks on the first banner carousel element.
        Parameters: None
        Returns: None
        """
        try:
            self.helper.click_element(SortValidCarouselLocators.BANNER_CAROUSEL_FIRST)
            self.logger.debug("Clicked on first carousel")
        except Exception as e:
            self.logger.error(f"Failed to click on first carousel: {str(e)}")
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
            self.helper.verify_in(SortValidCarouselLocators.FESTIVE_HEADING, str(self.excel.read_testcase_data(2,"testcase2")))
            self.logger.debug("Validated the product listing page is opened")
            self.screenshot.capture_element_screenshot(
                self.helper.get_element(SortValidCarouselLocators.FESTIVE_HEADING),
                "error_festive_page"
            )
        except Exception as e:
            self.logger.error(f"Failed to open product listing page: {str(e)}")
            self.screenshot.capture_element_screenshot(
                self.helper.get_element(SortValidCarouselLocators.FESTIVE_HEADING),
                "error_festive_page"
            )
            raise Exception(str(e))

    def select_filter_bestseller_action(self):
        """
        method name: select_filter_bestseller_action
        Author name: Ritika Bhardwaj
        description: Selects 'Bestseller' from the sort-by dropdown.
        parameter: None
        Return type: None
        """
        try:
            dropdown = Select(self.helper.get_element(SortValidCarouselLocators.SORT_BY_DROPDOWN))
            dropdown.select_by_value(str(self.excel.read_testcase_data(3,"testcase2")))
            self.logger.debug("Selected Bestseller from sort by dropdown")
        except Exception as e:
            self.logger.error(f"Failed to select bestseller from dropdown: {str(e)}")
            self.screenshot.capture_element_screenshot(self.helper.get_element(),"error_bestseller")
            raise Exception(str(e))

    def verify_bestseller_click_action(self):
        """
        method name: verify_bestseller_click_action
        Author name: Ritika Bhardwaj
        description: Verifies that 'Bestseller' is selected.
        parameter: None
        Return type: None
        """
        try:
            self.helper.verify_in(SortValidCarouselLocators.BESTSELLER_TEXT, str(self.excel.read_testcase_data(4,"testcase2")))
            self.logger.debug("Validated bestseller is been selected")
        except Exception as e:
            self.logger.error(f"Failed to select bestseller from sort by dropdown: {str(e)}")
            self.screenshot.capture_screenshot(self.driver, "error_bestseller")
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
            self.helper.js_scroll(SortValidCarouselLocators.SECOND_PRODUCT_DIV)
            self.driver.implicitly_wait(5)
            self.helper.hover_one_element(SortValidCarouselLocators.SECOND_PRODUCT_DIV)
            self.driver.implicitly_wait(5)
            self.helper.click_element(SortValidCarouselLocators.SECOND_PRODUCT)
            self.logger.debug("Clicked on second product")
        except Exception as e:
            self.logger.error(f"Failed to click second product: {str(e)}")
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
            self.helper.verify_in(SortValidCarouselLocators.SIZE_GUIDE_TEXT, str(self.excel.read_testcase_data(5,"testcase2")))
            self.logger.debug("Validated product page opened")
        except Exception as e:
            self.logger.error(f"Failed to open product page: {str(e)}")
            self.screenshot.capture_screenshot(self.driver, "error_first_product")
            raise Exception(str(e))

    def scroll_till_similar_product(self):
        """
        method name: scroll_till_similar_product
        Author name: Ritika Bhardwaj
        description: Scrolls to the similar product section and verifies heading.
        parameter: None
        Return type: None
        """
        try:
            sleep(3)
            self.helper.scroll_to_pixels(0,1500)
            sleep(2)
            self.helper.verify_in(SortValidCarouselLocators.SIMILAR_PRODUCT_HEADING,str(self.excel.read_testcase_data(6,"testcase2")))
            self.logger.debug("Scrolled till similar product")
        except Exception as e:
            self.logger.error(f"Failed to scroll till similar product: {str(e)}")
            self.screenshot.capture_screenshot(self.driver,"error_similar_product_heading")
            raise Exception (str(e))

    def click_first_similar_product(self):
        """
        method name: click_first_similar_product
        Author name: Ritika Bhardwaj
        description: Scrolls to and clicks the first similar product.
        parameter: None
        Return type: None
        """
        try:
            self.helper.js_scroll(SortValidCarouselLocators.FIRST_SIMILAR_PRODUCT)
            self.helper.click_element(SortValidCarouselLocators.FIRST_SIMILAR_PRODUCT)
            self.logger.debug("Clicked first similar product")
        except Exception as e:
            self.logger.error(f"Failed to click first similar product: {str(e)}")
            self.screenshot.capture_screenshot(self.driver,"error_first_similar_product")
            raise Exception (str(e))

    def verify_similar_product_page(self):
        """
        Method: verify_similar_product_page
        Author: Ritika Bhardwaj
        Description: Verifies that the product page is opened by checking for 'Size Guide' text.
        Parameters: None
        Returns: None
        """
        try:
            self.helper.switch_window()
            self.helper.verify_in(SortValidCarouselLocators.SIZE_GUIDE_TEXT, str(self.excel.read_testcase_data(7,"testcase2")))
            self.logger.debug("Validated product page opened")
        except Exception as e:
            self.logger.error(f"Failed to open product page: {str(e)}")
            self.screenshot.capture_screenshot(self.driver, "error_first_product")
            raise Exception(str(e))
