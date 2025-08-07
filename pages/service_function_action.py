from locators.service_function_locators import SearchFunctionLocators
from utilities.excelReader import ExcelReader
from time import sleep

class ServiceFunctionAction:
    def __init__(self, driver, helper, logger, screenshot):
        self.driver = driver
        self.helper = helper
        self.logger = logger
        self.screenshot = screenshot
        self.excel = ExcelReader("testdata/data.xlsx")

    def perform_action(self):
        try:
            self.logger.info("Verifying services related to Qutumb")
            self.hover_on_service()
            self.click_qutumb_service_option()
            self.scroll_to_contact_section()
            self.click_contact_banner()
            self.scroll_to_form_section()
            self.enter_full_name()
            self.enter_phone_number()
            self.click_generate_otp()
            self.logger.info("Successfully verified services related to Qutumb")
        except Exception as e:
            self.logger.error(f"Failed to verify services offered by fanindia: {str(e)}")

    def hover_on_service(self):
        """
        a. Method name: hover_on_service
        b. Author name: Ritika Bhardwaj
        c. Short description: Hovers over the 'Service' navigation menu.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.hover_one_element(SearchFunctionLocators.SERVICE_NAV)
            self.logger.debug("Hovered over the 'Service' navigation menu.")
        except Exception as e:
            self.logger.error(f"Failed to hover over the 'Service' navigation menu: {str(e)}")
            self.screenshot.capture_screenshot(self.driver,"error_hover_service")
            raise Exception (str(e))

    def click_qutumb_service_option(self):
        """
        a. Method name: click_qutumb_service_option
        b. Author name: Ritika Bhardwaj
        c. Short description: Clicks on the Qutumb section to navigate to contact.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.click_element(SearchFunctionLocators.QTUMB)
            self.logger.debug("Clicked on the Qutumb section.")
        except Exception as e:
            self.logger.error(f"Failed to click on the Qutumb section: {str(e)}")
            self.screenshot.capture_screenshot(self.driver,"error_qutumb_section")
            raise Exception (str(e))

    def scroll_to_contact_section(self):
        """
        a. Method name: scroll_to_contact_section
        b. Author name: Ritika Bhardwaj
        c. Short description: Scrolls to the contact section of the Qutumb page.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            sleep(2)
            self.helper.scroll_by_pixels(0,1500)
            sleep(4)
            self.logger.debug("Scrolled to the contact section.")
        except Exception as e:
            self.logger.error(f"Failed to scroll to the contact section: {str(e)}")
            self.screenshot.capture_screenshot(self.driver,"error_contact_section")
            raise Exception (str(e))

    def click_contact_banner(self):
        """
        a. Method name: click_contact_banner
        b. Author name: Ritika Bhardwaj
        c. Short description: Clicks on the contact banner to open the form.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.click_element(SearchFunctionLocators.CONTACT_BANNER)
            self.logger.debug("Clicked on the contact banner.")
        except Exception as e:
            self.logger.error(f"Failed to click on the contact banner.: {str(e)}")
            self.screenshot.capture_screenshot(self.driver,"error_contact_banner")
            raise Exception (str(e))

    def scroll_to_form_section(self):
        """
        a. Method name: scroll_to_form_section
        b. Author name: Ritika Bhardwaj
        c. Short description: Scrolls to the form section on the contact page.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            sleep(2)
            self.helper.scroll_by_pixels(0,600)
            sleep(3)
            self.logger.debug("Scrolled to the form section.")
        except Exception as e:
            self.logger.error(f"Failed to scroll to the form section: {str(e)}")
            self.screenshot.capture_screenshot(self.driver,"error_form_section")
            raise Exception (str(e))

    def enter_full_name(self):
        """
        a. Method name: enter_full_name
        b. Author name: Ritika Bhardwaj
        c. Short description: Enters the full name into the form field.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.click_element(SearchFunctionLocators.FULL_NAME)
            self.helper.fill_form(SearchFunctionLocators.FULL_NAME, str(self.excel.read_testcase_data(2,"testcase12")))
            self.logger.debug("Entered full name: Ritika Bhardwaj.")
        except Exception as e:
            self.logger.error(f"Failed to enter full name: {str(e)}")
            self.screenshot.capture_screenshot(self.driver,"error_enter_name")
            raise Exception (str(e))

    def enter_phone_number(self):
        """
        a. Method name: enter_phone_number
        b. Author name: Ritika Bhardwaj
        c. Short description: Enters an invalid phone number into the form field.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.click_element(SearchFunctionLocators.PHONE)
            self.helper.fill_form(SearchFunctionLocators.PHONE, str(self.excel.read_testcase_data(3,"testcase12")))
            self.logger.debug("Entered phone number: 9876543210")
        except Exception as e:
            self.logger.error(f"Failed to enter phone number: {str(e)}")
            self.screenshot.capture_screenshot(self.driver,"error_enter_phone")
            raise Exception (str(e))

    def click_generate_otp(self):
        """
        a. Method name: click_generate_otp
        b. Author name: Ritika Bhardwaj
        c. Short description: Clicks on the 'Generate OTP' button.
        d. Return type: None
        e. Parameter list: None
        """
        try:
            self.helper.click_element(SearchFunctionLocators.GENERATE_OTP)
            self.logger.debug("Clicked on 'Generate OTP' button.")
        except Exception as e:
            self.logger.error(f"Failed to click on 'Generate OTP' button: {str(e)}")
            self.screenshot.capture_screenshot(self.driver,"error_generate_otp")
            raise Exception (str(e))

