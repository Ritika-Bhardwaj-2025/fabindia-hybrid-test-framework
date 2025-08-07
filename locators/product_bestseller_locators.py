from selenium.webdriver.common.by import By

class ProductBestsellerLocators:
    BANNER_DIV = (By.XPATH, "(//div[@class='carousel-inner'])[1]")
    BANNER_CAROUSEL_FIRST = (By.XPATH, "(//div[@class='carousel-inner'])[1]/div[@data-bs-interval][1]")
    FESTIVE_HEADING = (By.TAG_NAME, "h1")
    SORT_BY_DROPDOWN = (By.ID, "select-filter")  # productCountBestSeller-desc (value)
    BESTSELLER_TEXT = (By.XPATH, "//option[text()=' Bestseller ']")

    SECOND_PRODUCT_DIV = (By.XPATH, "(//div[@class='custom-prod-desc'])[2]/a")
    SECOND_PRODUCT = (By.XPATH, "(//div[@class='custom-prod-desc'])[2]/a/p")
    SIZE_GUIDE_TEXT = (By.XPATH, "(//button[@class='border-0 bg-transparent'])[2]/span")