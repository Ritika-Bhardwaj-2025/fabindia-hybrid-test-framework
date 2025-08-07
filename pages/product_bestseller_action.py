from selenium.webdriver.support.select import Select
from locators.product_bestseller_locators import ProductBestsellerLocators
from utilities.excelReader import ExcelReader
from time import sleep

class ProductBestsellerAction:
    def __init__(self,driver,helper,logger,screenshot):
        self.driver = driver
        self.helper = helper
        self.logger = logger
        self.screenshot = screenshot
        self.excel = ExcelReader("testdata/data.xlsx")

    def perform_action(self):
        try:
            self.logger.info("Verifying product with filter bestseller")
            self.click_banner_carousel_action()
            self.verify_product_page_action()
            self.select_filter_bestseller_action()
            self.verify_bestseller_click_action()
            self.hover_click_second_product()
            self.verify_size_guide_action()
            self.logger.info("Successfully verified product with filter bestseller")
        except Exception as e:
            self.logger.error(f"Failed to verify product with filter bestseller: {str(e)}")


    def click_banner_carousel_action(self):
        """
        Method: click_banner_carousel_action
        Author: Ritika Bhardwaj
        Description: Clicks on the first banner carousel element.
        Parameters: None
        Returns: None
        """
        try:
            self.helper.click_element(ProductBestsellerLocators.BANNER_CAROUSEL_FIRST)
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
            self.helper.verify_in(ProductBestsellerLocators.FESTIVE_HEADING, str(self.excel.read_testcase_data(2,"testcase15")))
            self.logger.debug("Validated the product listing page is opened")
            self.screenshot.capture_element_screenshot(
                self.helper.get_element(ProductBestsellerLocators.FESTIVE_HEADING),
                "error_festive_page"
            )
        except Exception as e:
            self.logger.error(f"Failed to open product listing page: {str(e)}")
            self.screenshot.capture_element_screenshot(
                self.helper.get_element(ProductBestsellerLocators.FESTIVE_HEADING),
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
            dropdown = Select(self.helper.get_element(ProductBestsellerLocators.SORT_BY_DROPDOWN))
            dropdown.select_by_value(str(self.excel.read_testcase_data(3,"testcase15")))
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
            self.helper.verify_in(ProductBestsellerLocators.BESTSELLER_TEXT, str(self.excel.read_testcase_data(4,"testcase15")))
            self.logger.debug("validated bestseller is been selected")
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
            self.helper.js_scroll(ProductBestsellerLocators.SECOND_PRODUCT_DIV)
            self.driver.implicitly_wait(5)
            self.helper.hover_one_element(ProductBestsellerLocators.SECOND_PRODUCT_DIV)
            self.driver.implicitly_wait(5)
            self.helper.click_element(ProductBestsellerLocators.SECOND_PRODUCT)
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
            self.helper.verify_in(ProductBestsellerLocators.SIZE_GUIDE_TEXT, str(self.excel.read_testcase_data(5,"testcase15")))
            self.logger.debug("Validated product page opened")
        except Exception as e:
            self.logger.error(f"Failed to open product page: {str(e)}")
            self.screenshot.capture_screenshot(self.driver, "error_first_product")
            raise Exception(str(e))
