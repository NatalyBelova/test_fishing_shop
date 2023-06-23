import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    catalog_button = "//button[@class='header__btn-catalog btn btn-dark flb-csb']"
    type_product_button_1 = "/html/body/div[2]/div/nav[1]/div[5]/a/span"
    type_product_button_2 = "/html/body/main/div[2]/div/div/div[1]/a[7]"
    search_button = "//input[@name='search']"


    """Getters"""

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_type_product_button_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_product_button_1)))

    def get_type_product_button_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_product_button_2)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))


    """Actions"""

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click Catalog Button")

    def click_type_product_button_1(self):
        self.get_type_product_button_1().click()
        print("Click Type Product Button_1")

    def click_type_product_button_2(self):
        self.get_type_product_button_2().click()
        print("Click Type Product Button_2")

    def input_search_button(self, search):
        self.get_search_button().send_keys(search)
        print("Input Search Button")


    """Methods"""

    def select_menu(self):
        self.click_catalog_button()
        self.click_type_product_button_1()
        self.click_type_product_button_2()

    def search_1(self):
        self.input_search_button("Ласты")
        self.get_screenshot()
        self.driver.send_keys(Keys.RETURN)
        self.get_screenshot()

    def search_2(self):
        self.input_search_button("Блесна")
        self.get_screenshot()
        self.driver.send_keys(Keys.RETURN)
        self.get_screenshot()

    def search_3(self):
        self.input_search_button("Лодка")
        self.get_screenshot()
        self.driver.send_keys(Keys.RETURN)
        self.get_screenshot()












