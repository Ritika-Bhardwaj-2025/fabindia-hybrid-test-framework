from selenium.webdriver.common.by import By

class FirstCarouselLocators:
    FESTIVE_HEADING = (By.TAG_NAME,"h1")
    COLOR_DROPDOWN = (By.XPATH,"//button[text()=' Color ']")
    PINK_OPTION = (By.XPATH,"//label[text()=' Pink ']/parent::label")
    FIRST_PRODUCT_DIV = (By.XPATH, "(//div[@class='custom-prod-desc'])[1]/a")
    FIRST_PRODUCT = (By.XPATH, "(//div[@class='custom-prod-desc'])[1]/a/p")

    PRODUCT_TITLE = (By.CLASS_NAME,"prod_heading_title")
    SIZE_GUIDE_TEXT = (By.XPATH,"(//button[@class='border-0 bg-transparent'])[2]/span")
    ADD_TO_CART = (By.XPATH, "//button[text()='Add to cart ']")
    GO_TO_CART = (By.XPATH, "//button[text()=' Go to Cart ']")
