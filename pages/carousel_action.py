from locators.bannerLocators import BannerLocators
from locators.carousel_locators import FirstCarouselLocators
from utilities.excelReader import ExcelReader
from time import sleep

class ValidCarouselAction:
    def __init__(self, driver, helper, logger, screenshot):
        self.driver = driver
        self.helper = helper
        self.logger = logger
        self.screenshot = screenshot
        self.excel = ExcelReader("testdata/data.xlsx")

    def perform_action(self):
        try:
            self.logger.info("Verifying product with color filter is shown")
            self.click_banner_carousel_action()
            self.verify_product_page_action()
            self.click_color_dropdown_action()
            self.verify_color_dropdown()
            self.scroll_click_pink_option()
            self.verify_pink_option_action()
            self.hover_click_product_action()
            self.verify_size_guide_action()
            self.click_add_to_cart()
            self.logger.info("Successfully verified product with color filter is shown")
        except Exception as e:
            self.logger.error(f"Failed to verify product with color filter: {str(e)}")

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
            self.helper.verify_in(FirstCarouselLocators.FESTIVE_HEADING,
                                  str(self.excel.read_testcase_data(2,"testcase1")))
            self.logger.debug("Validated the product listing page is opened")
            self.screenshot.capture_element_screenshot(
                self.helper.get_element(FirstCarouselLocators.FESTIVE_HEADING),
                "error_festive_page"
            )
        except Exception as e:
            self.logger.error(f"Failed to open product listing page: {str(e)}")
            self.screenshot.capture_element_screenshot(
                self.helper.get_element(FirstCarouselLocators.FESTIVE_HEADING),
                "error_festive_page"
            )
            raise Exception(str(e))

    def click_color_dropdown_action(self):
        """
        Method: click_color_dropdown_action
        Author: Ritika Bhardwaj
        Description: Clicks on the color dropdown element.
        Parameters: None
        Returns: None
        """
        try:
            self.helper.click_element(FirstCarouselLocators.COLOR_DROPDOWN)
            self.logger.debug("Clicked on color dropdown")
        except Exception as e:
            self.logger.error(f"Failed to click color dropdown: {str(e)}")
            self.screenshot.capture_screenshot(self.driver, "error_click_color")
            raise Exception(str(e))

    def verify_color_dropdown(self):
        """
        Method: verify_color_dropdown
        Author: Ritika Bhardwaj
        Description: Verifies that the color dropdown was successfully clicked.
        Parameters: None
        Returns: None
        """
        try:
            self.helper.verify_in(FirstCarouselLocators.COLOR_DROPDOWN, str(self.excel.read_testcase_data(3,"testcase1")))
            self.logger.debug("Validated color dropdown is clicked")
        except Exception as e:
            self.logger.error(f"Failed to validate color dropdown: {str(e)}")
            self.screenshot.capture_element_screenshot(
                self.helper.get_element(FirstCarouselLocators.COLOR_DROPDOWN),
                "error_color_dropdown"
            )
            raise Exception(str(e))

    def scroll_click_pink_option(self):
        """
        Method: scroll_click_pink_option
        Author: Ritika Bhardwaj
        Description: Scrolls to and clicks the 'Pink' color option.
        Parameters: None
        Returns: None
        """
        try:
            sleep(2)
            self.helper.scroll_by_keys(FirstCarouselLocators.PINK_OPTION,5)
            sleep(2)
            self.driver.implicitly_wait(5)
            self.helper.click_element(FirstCarouselLocators.PINK_OPTION)
            self.logger.debug("Clicked on pink color option")
        except Exception as e:
            self.logger.error(f"Failed to click on pink option: {str(e)}")
            self.screenshot.capture_screenshot(self.driver, "error_click_pink")
            raise Exception(str(e))

    def verify_pink_option_action(self):
        """
        Method: verify_pink_option_action
        Author: Ritika Bhardwaj
        Description: Verifies that the 'Pink' option was selected.
        Parameters: None
        Returns: None
        """
        try:
            self.helper.verify_in(FirstCarouselLocators.PINK_OPTION, str(self.excel.read_testcase_data(4,"testcase1")))
            self.logger.debug("Validated pink option is clicked")
        except Exception as e:
            self.logger.error(f"Failed to verify pink option: {str(e)}")
            self.screenshot.capture_element_screenshot(
                self.helper.get_element(FirstCarouselLocators.PINK_OPTION),
                "error_pink_option"
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
            self.helper.scroll_by_keys(FirstCarouselLocators.FIRST_PRODUCT_DIV,5)
            sleep(2)
            self.helper.hover_one_element(FirstCarouselLocators.FIRST_PRODUCT_DIV)
            self.driver.implicitly_wait(5)
            self.helper.click_element(FirstCarouselLocators.FIRST_PRODUCT)
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
            self.helper.verify_in(FirstCarouselLocators.SIZE_GUIDE_TEXT, str(self.excel.read_testcase_data(5,"testcase1")))
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
            self.driver.implicitly_wait(5)
            self.helper.click_element(FirstCarouselLocators.ADD_TO_CART)
            self.logger.debug("Clicked on add to cart button")
        except Exception as e:
            self.logger.error(f"Failed to click add to cart: {str(e)}")
            self.screenshot.capture_screenshot(self.driver, "error_add_to_cart")
            raise Exception(str(e))
