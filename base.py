import pytest
from selenium import webdriver
from utilities.webDriverHelper import WebDriverHelper
from utilities.configReader import ConfigReader
from utilities.logger import setup_logzero_logger
from utilities.screenshot import ScreenShot
from pages.carousel_action import ValidCarouselAction
from pages.sort_filter_carousel_action import SortValidCarousel
from pages.fantastic_first_product_action import FantasticFirstProductAction
from pages.fantastic_last_product_action import FantasticLastProductAction
from pages.carousel_right_function_action import CarouselRightFunctionAction
from pages.carousel_arrow_function_actions import CarouselArrowFunctionAction
from pages.sort_price_carousel_action import SortPriceCarouselAction
from pages.festive_action import FestiveAction
from pages.add_to_cart_action import AddToCartAction
from pages.content_section_action import ContentSectionAction
from pages.men_jacket_action import MenJacketAction
from pages.service_function_action import ServiceFunctionAction
from pages.store_finder_action import StoreFinderAction
from pages.product_navigation_action import ProductNavigationAction
from pages.product_bestseller_action import ProductBestsellerAction
from pages.home_living_action import HomeLivingActions

logger = setup_logzero_logger()
@pytest.fixture
def set_up_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(ConfigReader().get_website())
    helper = WebDriverHelper(driver)
    screenshot = ScreenShot()
    yield driver, helper, screenshot

    driver.quit()

@pytest.mark.valid_carousel
def test_valid_carousel(set_up_driver):
    driver, helper, screenshot = set_up_driver
    actions = ValidCarouselAction(driver, helper, logger, screenshot)
    actions.perform_action()

@pytest.mark.sort_valid_carousel
def test_sort_valid_carousel(set_up_driver):
    driver, helper, screenshot = set_up_driver
    actions = SortValidCarousel(driver, helper, logger, screenshot)
    actions.perform_action()

@pytest.mark.fantastic_first_find
def test_fantastic_first_find(set_up_driver):
    driver, helper, screenshot = set_up_driver
    actions = FantasticFirstProductAction(driver, helper, logger, screenshot)
    actions.perform_action()

@pytest.mark.fantastic_last_find
def test_fantastic_last_find(set_up_driver):
    driver, helper, screenshot = set_up_driver
    actions = FantasticLastProductAction(driver, helper, logger, screenshot)
    actions.perform_action()

@pytest.mark.carousel_right_function
def test_carousel_right_function(set_up_driver):
    driver, helper, screenshot = set_up_driver
    actions = CarouselRightFunctionAction(driver, helper, logger, screenshot)
    actions.perform_action()

@pytest.mark.carousel_arrow_function
def test_carousel_arrow_function(set_up_driver):
    driver, helper, screenshot = set_up_driver
    actions = CarouselArrowFunctionAction(driver, helper, logger, screenshot)
    actions.perform_action()

@pytest.mark.sort_price_carousel
def test_sort_price_carousel(set_up_driver):
    driver, helper, screenshot = set_up_driver
    actions = SortPriceCarouselAction(driver, helper, logger, screenshot)
    actions.perform_action()

@pytest.mark.festive
def test_festive(set_up_driver):
    driver, helper, screenshot = set_up_driver
    actions = FestiveAction(driver, helper, logger, screenshot)
    actions.perform_action()

@pytest.mark.add_wishlist
def test_add_wishlist(set_up_driver):
    driver, helper, screenshot = set_up_driver
    actions = AddToCartAction(driver, helper, logger, screenshot)
    actions.perform_action()

@pytest.mark.content_section
def test_content_section(set_up_driver):
    driver, helper, screenshot = set_up_driver
    actions = ContentSectionAction(driver, helper, logger, screenshot)
    actions.perform_action()

@pytest.mark.men_jacket
def test_men_jacket(set_up_driver):
    driver, helper, screenshot = set_up_driver
    actions = MenJacketAction(driver, helper, logger, screenshot)
    actions.perform_action()

@pytest.mark.service_function
def test_service_function(set_up_driver):
    driver, helper, screenshot = set_up_driver
    actions = ServiceFunctionAction(driver, helper, logger, screenshot)
    actions.perform_action()

@pytest.mark.store_finder
def test_store_finder(set_up_driver):
    driver, helper, screenshot = set_up_driver
    actions = StoreFinderAction(driver, helper, logger, screenshot)
    actions.perform_action()

@pytest.mark.product_navigation
def test_product_navigation(set_up_driver):
    driver, helper, screenshot = set_up_driver
    actions = ProductNavigationAction(driver, helper, logger, screenshot)
    actions.perform_action()

@pytest.mark.product_bestseller
def test_product_bestseller(set_up_driver):
    driver, helper, screenshot = set_up_driver
    actions = ProductBestsellerAction(driver, helper, logger, screenshot)
    actions.perform_action()

@pytest.mark.home_living
def test_home_living(set_up_driver):
    driver, helper, screenshot = set_up_driver
    actions = HomeLivingActions(driver, helper, logger, screenshot)
    actions.perform_action()
