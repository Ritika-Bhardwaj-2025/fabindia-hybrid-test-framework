from selenium.webdriver.common.by import By

class BannerLocators:
    BANNER_DIV = (By.XPATH,"(//div[@class='carousel-inner'])[1]")
    BANNER_CAROUSEL_FIRST = (By.XPATH,"(//div[@class='carousel-inner'])[1]/div[@data-bs-interval][1]")
    BANNER_CAROUSEL_SECOND = (By.XPATH, "(//div[@class='carousel-inner'])[1]/div[@data-bs-interval][2]")
    BANNER_CAROUSEL_THIRD = (By.XPATH, "(//div[@class='carousel-inner'])[1]/div[@data-bs-interval][3]")
    BANNER_CAROUSEL_FOURTH = (By.XPATH, "(//div[@class='carousel-inner'])[1]/div[@data-bs-interval][4]")
    BANNER_CAROUSEL_FIFTH = (By.XPATH, "(//div[@class='carousel-inner'])[1]/div[@data-bs-interval][5]")
    ARROW_LEFT = (By.CLASS_NAME,"carousel-control-prev carousel-prev home-first-section-mob-icon")
    ARROW_RIGHT = (By.CLASS_NAME,"carousel-control-next carousel-next home-first-section-mob-icon")
