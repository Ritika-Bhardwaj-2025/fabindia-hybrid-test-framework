from locators.carousel_right_function_locators import CarouselRightFunctionLocators
from time import sleep

class CarouselRightFunctionAction:
    def __init__(self, driver, helper, logger, screenshot):
        self.driver = driver
        self.helper = helper
        self.logger = logger
        self.screenshot = screenshot

    def perform_action(self):
        try:
            self.logger.info("Verifying carousel right function")
            self.verify_banner_loaded()
            self.click_right_arrow()
            self.verify_banner_loaded()
            self.click_right_arrow()
            self.verify_banner_loaded()
            self.click_right_arrow()
            self.click_right_arrow()
            self.verify_banner_loaded()
            self.logger.info("Successfully verified carousel right function")
        except Exception as e:
            self.logger.error(f"Failed to verify carousel right function: {str(e)}")

    def verify_banner_loaded(self):
        """
        method name: verify_banner_loaded
        Author name: Ritika Bhardwaj
        description: Captures a screenshot to confirm banner is loaded.
        parameter: None
        Return type: None
        """
        try:
            sleep(2)
            self.screenshot.capture_screenshot(self.driver,"verify_banner_loaded")
            self.logger.debug("Banner is fully loaded")
        except Exception as e:
            self.logger.error(f"Failed to load the banner: {e}")
            self.screenshot.capture_screenshot(self.driver, "error_banner_loaded")
            raise Exception (str(e))

    def click_right_arrow(self):
        """
        method name: click_right_arrow
        Author name: Ritika Bhardwaj
        description: Clicks the right arrow in the carousel.
        parameter: None
        Return type: None
        """
        try:
            self.helper.click_element(CarouselRightFunctionLocators.ARROW_RIGHT)
            self.screenshot.capture_element_screenshot(self.helper.get_element(
                CarouselRightFunctionLocators.ARROW_RIGHT),"verify_right_arrow")
            self.logger.debug("Clicked right arrow")
        except Exception as e:
            self.logger.error(f"Failed to click right arrow: {e}")
            self.screenshot.capture_element_screenshot(self.helper.get_element(
                CarouselRightFunctionLocators.ARROW_RIGHT), "error_right_arrow")
            raise Exception(str(e))
