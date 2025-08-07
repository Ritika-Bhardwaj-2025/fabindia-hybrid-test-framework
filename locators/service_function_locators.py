from selenium.webdriver.common.by import By

class SearchFunctionLocators:
    SERVICE_NAV = (By.XPATH, "//p[text()='Services']")
    QTUMB = (By.XPATH, "//p[text()='Qutumb']")
    SCROLL_TO_CONTACT = (By.XPATH, "//h3[text()='Contact us']")
    CONTACT_BANNER = (By.XPATH, "(//img[@alt='qutumbh-sec05-11dec24-1.jpg'])[1]")
    SCROLL_TO_FORM_SECTION = (By.XPATH, "//h4[text()='Contact Form ']")
    FULL_NAME = (By.ID, 'ids_name')
    PHONE = (By.ID, 'phone')
    GENERATE_OTP = (By.XPATH, "//button[text()=' Generate OTP ']")
    VALIDATE_OTP = (By.XPATH, "//button[text()=' Invalid OTP ']")

