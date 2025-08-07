from selenium.webdriver.common.by import By

class MenJacketLocator:
    MEN_HOVER = (By.XPATH, "(//p[text()='Men'])[2]")
    JACKET_CLICK = (By.XPATH, "//a[@href='/clothing/men-jackets']")
    BUTTON_FILTER = (By.XPATH, "//button[text()=' Size ']")
    L_FILTER = (By.XPATH, "//label[text()=' L ']")
    FIRST_PRODUCT = (By.XPATH, "(//picture)[1]")
