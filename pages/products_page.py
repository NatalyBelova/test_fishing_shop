import time
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Products_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(driver)
        self.driver = driver


    """Locators"""

    filter_size = "/html/body/main/div[2]/div/aside/div[2]/div[4]/a/div"
    filter_size_check_box = "/html/body/main/div[2]/div/aside/div[2]/div[4]/div/label[3]/span[1]"
    filter_weight = "/html/body/main/div[2]/div/aside/div[2]/div[5]/a"
    filter_weight_check_box = "/html/body/main/div[2]/div/aside/div[2]/div[5]/div/label[2]/span[1]"
    add_to_cart_button = "//button[@class='product__item-add btn btn-orange product_id_addtocart_9152']"
    cart = "//a[@id='cart-header']"


    """Getters"""

    def get_filter_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_size)))

    def get_filter_size_check_box(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_size_check_box)))

    def get_filter_weight(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_weight)))

    def get_filter_weight_check_box(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_weight_check_box)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))


    """Actions"""

    def click_filter_size(self):
        self.get_filter_size().click()
        print("Click Filter Size")

    def click_filter_size_check_box(self):
        self.get_filter_size_check_box().click()
        print("Click Filter Size Check Box")

    def click_filter_weight(self):
        self.get_filter_weight().click()
        print("Click Filter Weight")

    def click_filter_weight_check_box(self):
        self.get_filter_weight_check_box().click()
        print("Click Filter Weight Check Box")

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Click Add To Cart Button")

    def click_cart(self):
        self.get_cart().click()
        print("Click Cart")


    """Methods"""

    def select_products(self):
        self.click_filter_size()
        self.click_filter_size_check_box()
        self.click_filter_weight()
        self.click_filter_weight_check_box()
        self.driver.execute_script("window.scrollTo(-1, 0)")
        time.sleep(1)
        self.click_add_to_cart_button()
        self.get_screenshot()
        self.click_cart()

