from selenium.webdriver.common.by import By

class SortPriceCarouselLocators:
    BANNER_DIV = (By.XPATH, "(//div[@class='carousel-inner'])[1]")
    BANNER_CAROUSEL_FIRST = (By.XPATH, "(//div[@class='carousel-inner'])[1]/div[@data-bs-interval][1]")
    FESTIVE_HEADING = (By.TAG_NAME, "h1")
    SORT_BY_DROPDOWN = (By.ID, "select-filter")  #price-desc (value)
    PRICE_HIGH_LOW_TEXT = (By.XPATH, "//option[text()=' Price: High to Low ']")

    SECOND_PRODUCT_DIV = (By.XPATH, "(//div[@class='custom-prod-desc'])[3]/a")
    SECOND_PRODUCT = (By.XPATH, "(//div[@class='custom-prod-desc'])[3]/a/p")
    SELECT_SIZE_TEXT = (By.CLASS_NAME, "pdp_size_div")
    SIMILAR_PRODUCT_HEADING = (By.XPATH,"//p[text()='Similar Product']")