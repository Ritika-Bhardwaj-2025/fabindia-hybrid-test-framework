from locators.content_section_locators import ContentSectionLocators
from utilities.excelReader import ExcelReader
from time import sleep

class ContentSectionAction:
    def __init__(self, driver, helper, logger, screenshot):
        self.driver = driver
        self.helper = helper
        self.logger = logger
        self.screenshot = screenshot
        self.excel = ExcelReader("testdata/data.xlsx")

    def perform_action(self):
        try:
            self.logger.info("Verifying content section scroll function")
            self.scroll_till_section()
            self.hover_content_section()
            self.scroll_women_collection()
            self.logger.info("Successfully verified content section scroll function")
        except Exception as e:
            self.logger.error(f"Failed to verify content section scroll: {str(e)}")

    def scroll_till_section(self):
        """
        method name: scroll_till_section
        Author name: Ritika Bhardwaj
        description: Scrolls the page to a fixed pixel position.
        parameter: None
        Return type: None
        """
        try:
            self.helper.scroll_to_pixels(0,3500)
            self.logger.debug("Scrolled till content section inner")
            sleep(2)
        except Exception as e:
            self.logger.error(f"Failed to scroll till section inner: {e}")
            self.screenshot.capture_screenshot(self.driver,"error_scroll_section")
            raise Exception(str(e))

    def hover_content_section(self):
        """
        method name: hover_content_section
        Author name: Ritika Bhardwaj
        description: Hovers over the content section element.
        parameter: None
        Return type: None
        """
        try:
            self.helper.hover_one_element(ContentSectionLocators.CONTENT_SECTION_DIV)
            self.logger.debug("Hovered over content section")
            sleep(2)
        except Exception as e:
            self.logger.error(f"Failed to hover over content section: {e}")
            self.screenshot.capture_screenshot(self.driver, "error_content_section")
            raise Exception(str(e))

    def scroll_women_collection(self):
        """
        method name: scroll_women_collection
        Author name: Ritika Bhardwaj
        description: Scrolls to women's heading and verifies text.
        parameter: None
        Return type: None
        """
        try:
            self.helper.js_scroll(ContentSectionLocators.WOMEN_HEADING)
            self.helper.verify_in(ContentSectionLocators.WOMEN_HEADING,str(self.excel.read_testcase_data(2,"testcase10")))
            self.logger.debug("Scrolled till women collection heading")
            sleep(5)
        except Exception as e:
            self.logger.error(f"Failed to scroll till women : {e}")
            self.screenshot.capture_screenshot(self.driver, "error_content_section")
            raise Exception(str(e))