from pages.main_page_page import MainPage
from pages.header_page import Header
from pages.search_results_page import SearchResults
# from pages.terms_and_conditions_page import TermsAndConditions
from pages.cart_page import CartPage
#from pages.product_page_page import ProductPage
# from pages.sign_in_page import SignInPage
# from pages.footer import Footer


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResults(self.driver)
        # self.terms_and_conditions_page = TermsAndConditions(self.driver)
        self.cart_page = CartPage(self.driver)
        #self.product_page_page = ProductPage(self.driver)
        # self.sign_in_page = SignInPage(self.driver)
        # self.footer = Footer(self.driver)

