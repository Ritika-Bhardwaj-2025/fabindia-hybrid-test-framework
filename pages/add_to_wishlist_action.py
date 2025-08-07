from locators.add_to_cart_locators import AddToCartLocators
from time import sleep
from utilities.webDriverHelper import WebDriverHelper
from utilities.screenshot import ScreenShot

class AddToWishlistAction:
    def __init__(self, driver, logger):
        self.driver = driver
        self.helper = WebDriverHelper(self.driver)
        self.logger = logger
        self.screenshot = ScreenShot()

    def click_banner_carousel_action(self):
        """
        Method: click_banner_carousel_action
        Author: Ritika Bhardwaj
        Description: Clicks on the first banner carousel element.
        Parameters: None
        Returns: None
        """
        self.logger.info("verifying add to wishlist functionality")
        try:
            self.helper.click_element(AddToCartLocators.BANNER_CAROUSEL_FIRST)
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
            self.helper.verify_in(AddToCartLocators.FESTIVE_HEADING, "Festive")
            self.logger.debug("Validated the product listing page is opened")
            self.screenshot.capture_element_screenshot(
                self.helper.get_element(AddToCartLocators.FESTIVE_HEADING),
                "error_festive_page"
            )
        except Exception as e:
            self.logger.error(f"Failed to open product listing page: {e}")
            self.screenshot.capture_element_screenshot(
                self.helper.get_element(AddToCartLocators.FESTIVE_HEADING),
                "error_festive_page"
            )
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
            self.helper.js_scroll(AddToCartLocators.SECOND_PRODUCT_DIV)
            self.driver.implicitly_wait(5)
            self.helper.hover_one_element(AddToCartLocators.SECOND_PRODUCT_DIV)
            self.driver.implicitly_wait(5)
            self.helper.click_element(AddToCartLocators.SECOND_PRODUCT)
            self.logger.debug("Clicked on second product")
        except Exception as e:
            self.logger.error(f"Failed to click second product: {e}")
            self.screenshot.capture_screenshot(self.driver, "error_second_product")
            raise Exception(str(e))

    def click_add_to_wishlist(self):
        """
        Method Name: click_add_to_wishlist
        Author: Ritika Bhardwaj
        Description: Clicks the 'Add to Wishlist' button.
        Parameters: None
        Return Type: None
        """
        try:
            self.helper.switch_window()
            self.helper.click_element(AddToCartLocators.ADD_WISHLIST)
            self.logger.debug("clicked add to wishlist button")
        except Exception as e:
            self.logger.error(f"Failed to click add to wishlist button: {e}")
            self.screenshot.capture_element_screenshot(self.helper.get_element(
                AddToCartLocators.ADD_WISHLIST),"error_add_wishlist")
            raise Exception(str(e))

    def verify_login_page(self):
        """
        Method Name: verify_login_page
        Author: Ritika Bhardwaj
        Description: Verifies the login page is opened.
        Parameters: None
        Return Type: None
        """
        try:
            self.helper.verify_in(AddToCartLocators.LOGIN_TEXT,"Login")
            self.logger.debug("validated login page opened")
            self.screenshot.capture_element_screenshot(self.helper.get_element(
                AddToCartLocators.LOGIN_TEXT), "verify_login_page")
        except Exception as e:
            self.logger.error(f"Failed to open login page: {e}")
            self.screenshot.capture_element_screenshot(self.helper.get_element(
                AddToCartLocators.LOGIN_TEXT), "error_login_page")
            raise Exception(str(e))

        self.logger.info("successfully verified add to wishlist functionality")
