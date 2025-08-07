from selenium.webdriver.common.by import By

class HomeLivingLocators:
    HOME_AND_LIVING = (By.XPATH, "(//p[text()='Home & Living'])[2]")
    LAMPS_LANTERNS = (By.XPATH, "//p[contains(text(),'Diyas, Lamps & Lanterns')]")
    LAMPS_TEXT = (By.XPATH, "//h1[text()=' Diyas, Lamps and Lanterns ']")
    COLOR_DROPDOWN = (By.XPATH, "//button[text()=' Color ']")
    MULTI_COLOR = (By.XPATH, "//label[text()=' Multi ']")
    CART_BTN = (By.XPATH, "//button[text()='Add to cart ']")
    FIRST_PRODUCT = (By.XPATH, "(//app-fab-product-grid-item)[1]")
