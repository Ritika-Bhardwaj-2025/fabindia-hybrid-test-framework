from locators.store_finder_locators import StoreFinderLocators
from utilities.excelReader import ExcelReader
from time import sleep

class StoreFinderAction:
    def __init__(self, driver, helper, logger, screenshot):
        self.driver = driver
        self.helper = helper
        self.logger = logger
        self.screenshot = screenshot
        self.excel = ExcelReader("testdata/data.xlsx")
        
    def perform_action(self):
        try:
            self.logger.info("Verifying store navigation functionality")
            self.click_on_store_icon()
            self.search_for_store()
            self.send_input_store_search_bar()
            self.verify_stores()
            self.logger.info("Successfully verified store navigation functionality")
        except Exception as e:
            self.logger.error(f"Failed to verify store navigation: {str(e)}")

    def click_on_store_icon(self):
        """
        a. Method name: click_on_store_icon
        b. Author name: Ritika Bhardwaj
        c. Short description of method: Clicks on the store icon to navigate to the store locator page.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.click_element(StoreFinderLocators.STORE_ICON)
            self.logger.debug("Clicked on store icon")
            sleep(1)
            self.helper.verify_in(StoreFinderLocators.VERIFY_STORES, str(self.excel.read_testcase_data(2,"testcase13")))
            self.logger.debug("Verified the store locator page")
        except Exception as e:
            self.logger.error(f"Not clicked on store icon: {str(e)}")
            self.screenshot.capture_screenshot(self.driver, "Not clicked on search icon")
            raise Exception(str(e))

    def search_for_store(self):
        """
        a. Method name: search_for_store
        b. Author name: Ritika Bhardwaj
        c. Short description of method: Scrolls and clicks on the store search bar, then verifies the store section.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.scroll_by_pixels(0, 300)
            sleep(2)
            self.helper.click_element(StoreFinderLocators.STORE_SEARCH_BAR)
            self.logger.debug("Clicked on search bar in home page")
            self.helper.verify_in(StoreFinderLocators.VERIFY_STORES,str(self.excel.read_testcase_data(3,"testcase13")))
            self.logger.debug("Verified the entering input into search bar")
        except Exception as e:
            self.logger.error(f"Not clicked on search bar: {str(e)}")
            self.screenshot.capture_screenshot(self.driver, 'clicked on search bar ')
            raise Exception(str(e))

    def send_input_store_search_bar(self):
        """
        a. Method name: send_input_store_search_bar
        b. Author name: Ritika Bhardwaj
        c. Short description of method: Sends input '5111' into the store search bar and captures a screenshot.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.fill_form_enter(StoreFinderLocators.STORE_SEARCH_BAR, str(self.excel.read_testcase_data(4,"testcase13")))
            self.screenshot.capture_screenshot(self.driver,"enter_value_store")
            self.logger.debug("Entered the input into search bar")
        except Exception as e:
            self.logger.error(f"Input not entered: {str(e)}")
            self.screenshot.capture_screenshot(self.driver,"error_input_not_send")
            raise Exception(str(e))

    def verify_stores(self):
        """
        a. Method name: verify_stores
        b. Author name: Ritika Bhardwaj
        c. Short description of method: Verifies if the 'No store found' message is displayed.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.verify_in(StoreFinderLocators.VERIFY_ERROR_MESSAGE, str(self.excel.read_testcase_data(5,"testcase13")))
            self.logger.debug("Verified the stores displayed")
        except Exception as e:
            self.logger.error(f"Not verified the stores: {str(e)}")
            self.screenshot.capture_screenshot(self.driver,"error_verify_store")
            raise Exception(str(e))

