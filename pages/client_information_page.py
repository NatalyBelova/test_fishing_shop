import time
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from faker import Faker

from utilities.logger import Logger


class Client_information_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    last_name = "//input[@name='name_second']"
    surname = "//input[@name='name_patronymic']"
    number_phone = "/html/body/main/div[2]/form/div/div/div[7]/div/input"
    delivery_method_button_1 = "/html/body/main/div[2]/form/div/div/div[9]/div/div/div[1]"
    delivery_method_button_2 = "/html/body/main/div[2]/form/div/div/div[9]/div/div/div[2]/div[1]"
    payment_method_button_1 = "/html/body/main/div[2]/form/div/div/div[10]/div/div/div[1]"
    payment_method_button_2 = "/html/body/main/div[2]/form/div/div/div[10]/div/div/div[2]/div[2]"
    region = "//input[@name='adress_region']"
    area = "//input[@name='adress_district']"
    city = "//input[@name='adress_city']"
    address = "//input[@name='adress_all']"
    index = "//input[@name='adress_idex']"
    checkout_button = "//button[@class='order__form-submit btn-submit btn btn-orange mb10']"


    """Getters"""

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_surname(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.surname)))

    def get_number_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_phone)))

    def get_delivery_method_button_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_method_button_1)))

    def get_delivery_method_button_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_method_button_2)))

    def get_payment_method_button_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_method_button_1)))

    def get_payment_method_button_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_method_button_2)))

    def get_region(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.region)))

    def get_area(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.area)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_index(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.index)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    """Actions"""

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input Last Name")

    def input_surname(self, surname):
        self.get_surname().send_keys(surname)
        print("Input Surname")

    def input_number_phone(self, number_phone):
        self.get_number_phone().send_keys(number_phone)
        print("Input Number Phone")

    def click_delivery_method_button_1(self):
        self.get_delivery_method_button_1().click()
        print("CLick Delivery Method Button_1")

    def click_delivery_method_button_2(self):
        self.get_delivery_method_button_2().click()
        print("CLick Delivery Method Button_2")

    def click_payment_method_button_1(self):
        self.get_payment_method_button_1().click()
        print("CLick Payment Method Button_1")

    def click_payment_method_button_2(self):
        self.get_payment_method_button_2().click()
        print("CLick Payment Method Button_2")

    def input_region(self, region):
        self.get_region().send_keys(region)
        print("Input Region")

    def input_area(self, area):
        self.get_area().send_keys(area)
        print("Input Area")

    def input_city(self, city):
        self.get_city().send_keys(city)
        print("Input City")

    def input_address(self, address):
        self.get_address().send_keys(address)
        print("Input Address")

    def input_index(self, index):
        self.get_index().send_keys(index)
        print("Input Index")

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("CLick Checkout Button")


    """Methods"""

    """Заполняем данные о клиенте для оформления заказа"""
    def client_information(self):
        Logger.add_start_step(method='client_information')
        fake = Faker("ru_RU")
        self.input_last_name("Иванов")
        self.input_surname("Иванович")
        self.input_number_phone("+71112223344")
        self.click_delivery_method_button_1()
        self.click_delivery_method_button_2()
        self.click_payment_method_button_1()
        self.click_payment_method_button_2()
        self.input_region("-")
        self.input_area(fake.street_name())
        self.input_city(fake.city())
        self.input_address(fake.address())
        self.input_index(fake.postcode())
        self.driver.execute_script("window.scrollTo(0, 350)")
        self.get_screenshot()
        self.click_checkout_button()
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method='client_information')


