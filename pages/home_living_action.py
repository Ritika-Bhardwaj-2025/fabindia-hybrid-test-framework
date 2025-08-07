from locators.home_living_locators import HomeLivingLocators
from utilities.excelReader import ExcelReader
from time import sleep

class HomeLivingActions:
    def __init__(self, driver, helper, logger, screenshot):
        self.driver = driver
        self.helper = helper
        self.logger = logger
        self.screen_shot = screenshot
        self.excel = ExcelReader("testdata/data.xlsx")

    def perform_action(self):
        try:
            self.logger.info("Verifying product from home and living section")
            self.hover_home_living()
            self.click_lamps_lanterns()
            self.click_dropdown()
            self.select_multicolor_option()
            self.click_first_product()
            self.click_add_to_cart()
            self.logger.info("Successfully verified product from home & living section")
        except Exception as e:
            self.logger.error(f"Failed to verify product from home and living services: {str(e)}")

    def hover_home_living(self):
        """
        a. Method name: hover_home_living
        b. Author name: Ritika Bhardwaj
        c. Short description of method: Clicks on the Home & Living section.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.hover_one_element(HomeLivingLocators.HOME_AND_LIVING)
            self.helper.verify_in(HomeLivingLocators.HOME_AND_LIVING, str(self.excel.read_testcase_data(2,"testcase16")))
            self.logger.debug("Clicked on Home & Living section")
        except Exception as e:
            self.logger.error(f"Failed to click on hover_home_living: {str(e)}")
            self.screen_shot.capture_screenshot(self.driver, "error_home_living")
            raise Exception(str(e))

    def click_lamps_lanterns(self):
        """
        a. Method name: click_lamps_lanterns
        b. Author name: Ritika Bhardwaj
        c. Short description of method: Clicks on the Lamps & Lanterns category.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.click_element(HomeLivingLocators.LAMPS_LANTERNS)
            sleep(3)
            self.helper.verify_in(HomeLivingLocators.LAMPS_TEXT,str(self.excel.read_testcase_data(3,"testcase16")))
            self.logger.debug("Clicked on Lamps & Lanterns")
        except Exception as e:
            self.logger.error(f"Failed to click on lamps and lanterns: {str(e)}")
            self.screen_shot.capture_screenshot(self.driver, "error_lamps")
            raise Exception(str(e))

    def click_dropdown(self):
        """
        a. Method name: click_dropdown
        b. Author name: Ritika Bhardwaj
        c. Short description of method: Clicks the color filter dropdown.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.click_element(HomeLivingLocators.COLOR_DROPDOWN)
            self.helper.verify_in(HomeLivingLocators.COLOR_DROPDOWN, str(self.excel.read_testcase_data(4,"testcase16")))
            self.helper.js_scroll(HomeLivingLocators.COLOR_DROPDOWN)
            sleep(2)
            self.logger.debug("Clicked on color dropdown")
        except Exception as e:
            self.logger.error(f"Failed to click on dropdown: {str(e)}")
            self.screen_shot.capture_screenshot(self.driver, "error_color_dropdown")
            raise Exception(str(e))

    def select_multicolor_option(self):
        """
        a. Method name: select_multicolor_option
        b. Author name: Ritika Bhardwaj
        c. Short description of method: Selects the multicolor option from the dropdown.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.click_element(HomeLivingLocators.MULTI_COLOR)
            self.helper.verify_in(HomeLivingLocators.MULTI_COLOR, str(self.excel.read_testcase_data(5,"testcase16")))
            self.logger.debug("Selected multicolor option")
        except Exception as e:
            self.logger.error(f"Failed to select multicolor option: {str(e)}")
            self.screen_shot.capture_screenshot(self.driver, "error_multicolor")
            raise Exception(str(e))

    def click_first_product(self):
        """
        a. Method name: click_first_product
        b. Author name: Ritika Bhardwaj
        c. Short description of method: Clicks the first lamp product and switches to the new window.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.click_element(HomeLivingLocators.FIRST_PRODUCT)
            self.helper.switch_window()
            self.logger.debug("Clicked first product and switched to new window")
        except Exception as e:
            self.logger.error(f"Failed to click on first product: {str(e)}")
            self.screen_shot.capture_screenshot(self.driver, "error_first_product")
            raise Exception("error: " + str(e))

    def click_add_to_cart(self):
        """
        a. Method name: click_add_to_cart
        b. Author name: Ritika Bhardwaj
        c. Short description of method: Clicks the cart button to add the lamp to the cart.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.click_element(HomeLivingLocators.CART_BTN)
            self.logger.debug("Clicked on cart button")
        except Exception as e:
            self.logger.error(f"error occurred in add_to_cart: {str(e)}")
            self.screen_shot.capture_screenshot(self.driver, "error_add_to_cart")
            raise Exception(str(e))
