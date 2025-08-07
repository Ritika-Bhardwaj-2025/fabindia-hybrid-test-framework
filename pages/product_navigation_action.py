from locators.bannerLocators import BannerLocators
from locators.product_navigation_locators import ProductNavigationLocators
from utilities.excelReader import ExcelReader
from time import sleep

class ProductNavigationAction:
    def __init__(self, driver, helper, logger, screenshot):
        self.driver = driver
        self.helper = helper
        self.logger = logger
        self.screenshot = screenshot
        self.excel = ExcelReader("testdata/data.xlsx")

    def perform_action(self):
        try:
            self.logger.info("Verifying product navigation")
            self.click_banner_carousel_action()
            self.verify_product_page_action()
            self.hover_click_product_action()
            self.verify_size_guide_action()
            self.click_add_to_cart()
            self.logger.info("Successfully verified product navigation")
        except Exception as e:
            self.logger.error(f"Failed to verify product navigation: {str(e)}")

    def click_banner_carousel_action(self):
        """
        Method: click_banner_carousel_action
        Author: Ritika Bhardwaj
        Description: Clicks on the first banner carousel element.
        Parameters: None
        Returns: None
        """
        try:
            self.helper.click_element(BannerLocators.BANNER_CAROUSEL_FIRST)
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
            self.helper.verify_in(ProductNavigationLocators.FESTIVE_HEADING, str(self.excel.read_testcase_data(2,"testcase14")))
            self.logger.debug("Validated the product listing page is opened")
            self.screenshot.capture_element_screenshot(
                self.helper.get_element(ProductNavigationLocators.FESTIVE_HEADING),
                "error_festive_page"
            )
        except Exception as e:
            self.logger.error(f"Failed to open product listing page: {str(e)}")
            self.screenshot.capture_element_screenshot(
                self.helper.get_element(ProductNavigationLocators.FESTIVE_HEADING),
                "error_festive_page"
            )
            raise Exception(str(e))

    def hover_click_product_action(self):
        """
        Method: hover_click_product_action
        Author: Ritika Bhardwaj
        Description: Hovers over the first product and clicks it.
        Parameters: None
        Returns: None
        """
        sleep(3)
        try:
            self.helper.scroll_by_keys(ProductNavigationLocators.FIRST_PRODUCT_DIV,5)
            sleep(2)
            self.helper.hover_one_element(ProductNavigationLocators.FIRST_PRODUCT_DIV)
            self.driver.implicitly_wait(5)
            self.helper.click_element(ProductNavigationLocators.FIRST_PRODUCT)
            self.logger.debug("Clicked on first product from listing page")
        except Exception as e:
            self.logger.error(f"Failed to click first product: {str(e)}")
            self.screenshot.capture_screenshot(self.driver, "error_first_product")
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
            self.helper.verify_in(ProductNavigationLocators.SIZE_GUIDE_TEXT, str(self.excel.read_testcase_data(3,"testcase14")))
            self.logger.debug("Validated product page opened by verifying size guide text")
        except Exception as e:
            self.logger.error(f"Failed to open product page: {str(e)}")
            self.screenshot.capture_screenshot(self.driver, "error_first_product")
            raise Exception(str(e))

    def click_add_to_cart(self):
        """
        Method: click_add_to_cart
        Author: Ritika Bhardwaj
        Description: Clicks the 'Add to Cart' button on the product page.
        Parameters: None
        Returns: None
        """
        try:
            self.helper.js_scroll(ProductNavigationLocators.ADD_TO_CART)
            self.driver.implicitly_wait(5)
            self.helper.click_element(ProductNavigationLocators.ADD_TO_CART)
            self.logger.debug("Clicked on add to cart button")
        except Exception as e:
            self.logger.error(f"Failed to click add to cart: {str(e)}")
            self.screenshot.capture_screenshot(self.driver, "error_add_to_cart")
            raise Exception(str(e))