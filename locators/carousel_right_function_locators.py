from selenium.webdriver.common.by import By

class CarouselRightFunctionLocators:
    BANNER_DIV = (By.XPATH,"(//div[@class='carousel-inner'])[1]")
    BANNER_CAROUSEL_FIRST = (By.XPATH, "(//div[@class='carousel-inner'])[1]/div[@data-bs-interval][1]")
    ARROW_RIGHT = (By.ID,"caoursel-btn")
