from selenium.webdriver.common.by import By

class CarouselArrowFunctionLocators:
    BANNER_DIV = (By.XPATH,"(//div[@class='carousel-inner'])[1]")
    BANNER_CAROUSEL_FIRST = (By.XPATH, "(//div[@class='carousel-inner'])[1]/div[@data-bs-interval][1]")
    ARROW_LEFT = (By.XPATH,"//a[@class='carousel-control-prev carousel-prev home-first-section-mob-icon']")
    ARROW_RIGHT = (By.ID,"caoursel-btn")