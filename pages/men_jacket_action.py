from locators.men_jacket_locators import MenJacketLocator
from utilities.excelReader import ExcelReader
from time import sleep

class MenJacketAction:
    def __init__(self, driver, helper, logger, screenshot):
        self.driver = driver
        self.helper = helper
        self.logger = logger
        self.screenshot = screenshot
        self.excel = ExcelReader("testdata/data.xlsx")
        
    def perform_action(self):
        try:
            self.logger.info("Verifying men jacket product")
            self.hover_on_men()
            self.click_jacket_option()
            self.click_button_filter_size()
            self.click_l_size_option()
            self.click_first_product()
            self.logger.info("Successfully verified men jacket product")
        except Exception as e:
            self.logger.error(f"Failed to verify men jacket product: {str(e)}")

    def hover_on_men(self):
        """
        a. Method name: hover_on_men
        b. Author name: Ritika Bhardwaj
        c. Short description: Hovers over the 'Men' section in the navigation menu.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.hover_one_element(MenJacketLocator.MEN_HOVER)
            self.logger.debug("Hovered over the 'Men' section.")
        except Exception as e:
            self.logger.error(f"Failed to hover over the 'Men' section: {str(e)}")
            self.screenshot.capture_screenshot(self.driver,"error_hover_men")
            raise Exception (str(e))

    def click_jacket_option(self):
        """
        a. Method name: click_jacket_option
        b. Author name: Ritika Bhardwaj
        c. Short description: Clicks on the 'Jackets' category under Men.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.click_element(MenJacketLocator.JACKET_CLICK)
            self.logger.debug("Clicked on the 'Jackets' category.")
        except Exception as e:
            self.logger.error(f"Failed to click on the 'Jackets' category: {str(e)}")
            self.screenshot.capture_screenshot(self.driver,"error_click_jacket")
            raise Exception (str(e))

    def click_button_filter_size(self):
        """
        a. Method name: click_button_filter_size
        b. Author name: Ritika Bhardwaj
        c. Short description: Opens the filter options for jackets.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.click_element(MenJacketLocator.BUTTON_FILTER)
            self.logger.debug("Opened the filter options.")
        except Exception as e:
            self.logger.error(f"Failed to open the filter options: {str(e)}")
            self.screenshot.capture_screenshot(self.driver,"error_filter_size")
            raise Exception (str(e))

    def click_l_size_option(self):
        """
        a. Method name: click_l_size_option
        b. Author name: Ritika Bhardwaj
        c. Short description: Applies the 'L' size filter to the jacket listings.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.click_element(MenJacketLocator.L_FILTER)
            self.logger.debug("Applied the 'L' size filter.")
        except Exception as e:
            self.logger.error("Failed to apply the 'L' size filter.")
            raise Exception

    def click_first_product(self):
        """
        a. Method name: click_first_product
        b. Author name: Ritika Bhardwaj
        c. Short description: Clicks on the first product from the filtered jacket results.
        d. Return type: None
        e. Parameter list: None
        """
        sleep(7)
        try:
            self.helper.click_element(MenJacketLocator.FIRST_PRODUCT)
            self.logger.debug("Clicked on the first filtered product.")
        except Exception as e:
            self.logger.error(f"Failed to click on the first filtered product: {str(e)}")
            self.screenshot.capture_screenshot(self.driver,"error_click_product")
            raise Exception (str(e))

