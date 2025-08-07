from selenium.webdriver.common.by import By

class FantasticFirstProductLocators:
    FANTASTIC_FINDS_HEADING = (By.XPATH,"(//p[text()='Fantastic Finds'])[2]")
    FIRST_PRODUCT = (By.XPATH,"(//div[@id ='FabHomepageSection13Component']/descendant::a)[1]")
    PRODUCT_PAGE_HEADING = (By.TAG_NAME,"h1")
    THIRD_PRODUCT_DIV = (By.XPATH,"(//div[@class='custom-prod-desc'])[3]/a")
    THIRD_PRODUCT = (By.XPATH, "(//div[@class='custom-prod-desc'])[3]/a/p")
    SELECT_SIZE_TEXT = (By.CLASS_NAME, "pdp_size_div")

