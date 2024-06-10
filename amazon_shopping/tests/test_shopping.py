import pytest
from pytest_bdd import scenarios, given, when, then
from pages.homepage import HomePage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage


scenarios('features/shopping.feature')

PRODUCT_NAME = "laptop"
DESIRED_QUANTITY = 3

# fixtures created for each page that is used in the test
@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def product_page(page):
    return ProductPage(page)

@pytest.fixture
def basket_page(page):
    return BasketPage(page)

#test steps - definitions written in Gherkin format
@given('the user is on the Amazon homepage')
def navigate_to_homepage(home_page):
    home_page.navigate()

@when('the user searches for a product')
def search_for_product(home_page):
    home_page.search_product(PRODUCT_NAME)

@when('the user adds the product to the basket')
def add_product_to_basket(product_page):
    product_page.add_to_basket()
    product_page.navigate_to_basket()

@when('the user updates the quantity of the product in the basket to the desired quantity')
def update_quantity(basket_page):
    basket_page.update_quantity(DESIRED_QUANTITY)

@then('the basket should reflect the updated quantity')
def verify_quantity(basket_page):
    assert basket_page.get_quantity() == DESIRED_QUANTITY

@then('the total price should be updated accordingly')  
def verify_total_price(basket_page):
    assert basket_page.get_total_price()  == basket_page.calculate_expected_price()
