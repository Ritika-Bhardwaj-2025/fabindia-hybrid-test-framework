from selenium.webdriver.common.by import By

class ContentSectionLocators:
    CONTENT_SECTION_DIV = (By.XPATH,"//div[@class='top_content_section_inner']")
    WOMEN_HEADING = (By.XPATH,"//h2[contains(text(),'Women')]")