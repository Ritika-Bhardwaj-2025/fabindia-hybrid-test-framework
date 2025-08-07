from selenium.webdriver.common.by import By

class AddToCartLocators:
    BANNER_DIV = (By.XPATH, "(//div[@class='carousel-inner'])[1]")
    BANNER_CAROUSEL_FIRST = (By.XPATH, "(//div[@class='carousel-inner'])[1]/div[@data-bs-interval][1]")
    FESTIVE_HEADING = (By.TAG_NAME, "h1")
    SECOND_PRODUCT_DIV = (By.XPATH, "(//div[@class='custom-prod-desc'])[2]/a")
    SECOND_PRODUCT = (By.XPATH, "(//div[@class='custom-prod-desc'])[2]/a/p")
    ADD_WISHLIST = (By.XPATH,"//button[@class='btn button-add add_wishlist px-3 font-weight-bold mr-2']")
    LOGIN_TEXT = (By.XPATH,"//div[@class='mb-2 d-flex justify-content-between login-label']/span")