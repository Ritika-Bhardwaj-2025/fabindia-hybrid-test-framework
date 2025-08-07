# "1. Click the right arrow on the homepage banner until the third banner is displayed
# 2. Verify that the third banner is fully loaded
# 3. Click the CTA on the third banner (e.g., ""Shop Now"", ""Explore Now"")
# 4. Verify that the user is navigated to the correct landing page
# 5. Verify that the landing page URL and banner content match the CTA intent"

from selenium.webdriver.common.by import By

class FestiveLocators:
    BANNER_DIV = (By.XPATH, "(//div[@class='carousel-inner'])[1]")
    BANNER_CAROUSEL_THIRD = (By.XPATH, "(//div[@class='carousel-inner'])[1]/div[@data-bs-interval][3]")
    ARROW_RIGHT = (By.ID, "caoursel-btn")
    PRODUCT_PAGE_TITLE = (By.TAG_NAME,"h1")
    CURRENT_PAGE_URL = "https://www.fabindia.com/shop/all-products?query=:creationtime-desc:allCategories:all-products:category:kurtas:category:short%20kurtas:category:kurtis&sortCode=productCountBestSeller-desc&promoname=Kurtas&promoID=homemainBanner3"
