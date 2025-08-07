from selenium.webdriver.common.by import By

class StoreFinderLocators:
    STORE_ICON = (By.XPATH, "//button[@class='border-0 bg-transparent pr-sm-4 locator-icon']")
    VERIFY_STORES = (By.XPATH, "//span[text()='Stores']")
    STORE_SEARCH_BAR = (By.ID, 'searchInput1')
    VERIFY_BENGALURU = (By.XPATH, "//h5[text()=' Bengaluru - 30 ']")
    VERIFY_ERROR_MESSAGE = (By.XPATH, "//p[text()=' No store found ']")
    VIEW_DETAILS_OF_STORE = (By.XPATH, "(//a/child::button)[1]")
    MAP = (By.XPATH, "//button[text()='Map']")
