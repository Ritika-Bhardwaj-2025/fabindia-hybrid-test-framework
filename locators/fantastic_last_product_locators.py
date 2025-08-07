from selenium.webdriver.common.by import By

class FantasticLastProductLocators:
    FANTASTIC_FINDS_HEADING = (By.XPATH,"(//p[text()='Fantastic Finds'])[2]")
    RIGHT_ARROW = (By.XPATH,"(//a[@class='carousel-control-next new-Women-carousel-next-icon'])[2]")
    FOURTH_PRODUCT = (By.XPATH,"(//div[@id ='FabHomepageSection13Component']/descendant::a)[4]")
    PRODUCT_PAGE_HEADING = (By.TAG_NAME,"h1")